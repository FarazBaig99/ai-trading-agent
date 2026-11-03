import os
import asyncio
import webbrowser
from aiohttp import web
from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatGoogle

load_dotenv()

MAIN_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
FALLBACK_MODEL = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-3.5-flash-lite")

# Is folder mein browser ka profile (cookies, login) save hoga.
# Ek dafa login ho jaye, agli dafa login yaad rahega.
PROFILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iq_profile")

LOGIN_URL = "https://iqoption.com/ur/login?redirect_url=traderoom"

# Chat box is address par khulega
CHAT_PORT = int(os.getenv("CHAT_PORT", "8765"))

# Har chat message ke saath agent ko yeh yaad dilaya jata hai
CREDENTIALS_HINT = (
    "(If you need to log in to IQ Option, type x_email into the email/phone field "
    "and x_password into the password field. If a captcha or 2FA code is asked, "
    "stop and ask the user.)"
)

CHAT_PAGE = """<!doctype html>
<html lang="ur">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trading Agent Chat</title>
<style>
  :root { --bg:#f5f5f4; --panel:#fff; --text:#1c1917; --muted:#78716c;
          --me:#2563eb; --me-text:#fff; --agent:#e7e5e4; --border:#d6d3d1; }
  @media (prefers-color-scheme: dark) {
    :root { --bg:#1c1917; --panel:#292524; --text:#f5f5f4; --muted:#a8a29e;
            --me:#3b82f6; --me-text:#fff; --agent:#44403c; --border:#57534e; }
  }
  * { box-sizing: border-box; }
  body { margin:0; height:100vh; display:flex; flex-direction:column;
         background:var(--bg); color:var(--text); font:15px/1.5 system-ui, sans-serif; }
  header { padding:12px 16px; border-bottom:1px solid var(--border); background:var(--panel); }
  header b { display:block; }
  header small { color:var(--muted); }
  #log { flex:1; overflow-y:auto; padding:16px; display:flex; flex-direction:column; gap:10px; }
  .msg { max-width:85%; padding:8px 12px; border-radius:12px; white-space:pre-wrap; word-wrap:break-word; }
  .me { align-self:flex-end; background:var(--me); color:var(--me-text); }
  .agent { align-self:flex-start; background:var(--agent); }
  .info { align-self:center; color:var(--muted); font-size:13px; }
  form { display:flex; gap:8px; padding:12px; border-top:1px solid var(--border); background:var(--panel); }
  textarea { flex:1; resize:none; height:44px; padding:10px; border-radius:8px; font:inherit;
             border:1px solid var(--border); background:var(--bg); color:var(--text); }
  button { padding:0 18px; border:0; border-radius:8px; background:var(--me); color:var(--me-text); font:inherit; cursor:pointer; }
  button:disabled { opacity:.5; cursor:default; }
</style>
</head>
<body>
<header>
  <b>Trading Agent</b>
  <small id="status">Browser khul raha hai...</small>
</header>
<div id="log"></div>
<form id="form">
  <textarea id="input" placeholder="Hukam likhein, jaise: login karo" autofocus></textarea>
  <button id="send">Bhejo</button>
</form>
<script>
const log = document.getElementById('log');
const input = document.getElementById('input');
const send = document.getElementById('send');
const statusEl = document.getElementById('status');
let busy = false;

function add(text, cls) {
  const div = document.createElement('div');
  div.className = 'msg ' + cls;
  div.textContent = text;
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
}

function setBusy(on, label) {
  busy = on;
  send.disabled = on;
  statusEl.textContent = label;
}

async function sendMessage() {
  const text = input.value.trim();
  if (!text || busy) return;
  input.value = '';
  add(text, 'me');
  setBusy(true, 'Agent kaam kar raha hai...');
  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: text}),
    });
    const data = await res.json();
    add(data.reply, 'agent');
  } catch (e) {
    add('Agent se rabta nahi ho saka: ' + e, 'info');
  }
  setBusy(false, 'Tayyar');
}

document.getElementById('form').addEventListener('submit', e => { e.preventDefault(); sendMessage(); });
input.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
});

// Pehla task (login page kholna) khatam hone tak intezar
(async function waitReady() {
  setBusy(true, 'Browser khul raha hai...');
  while (true) {
    try {
      const data = await (await fetch('/status')).json();
      if (data.ready) {
        if (data.first_reply) add(data.first_reply, 'agent');
        add('Ab hukam dein, jaise: "login karo"', 'info');
        setBusy(false, 'Tayyar');
        return;
      }
    } catch (e) {}
    await new Promise(r => setTimeout(r, 1500));
  }
})();
</script>
</body>
</html>
"""


def result_text(history) -> str:
    final = history.final_result()
    if final:
        return final
    text = "Agent task complete nahi kar saka."
    errors = [e for e in history.errors() if e]
    if errors:
        text += f"\nLast error: {errors[-1]}"
    return text


class ChatServer:
    """Chat page aur agent ke darmiyan pul. Ek waqt mein ek hi task chalta hai."""

    def __init__(self, agent: Agent):
        self.agent = agent
        self.lock = asyncio.Lock()
        self.ready = False
        self.first_reply = ""

    async def run_first_task(self):
        async with self.lock:
            try:
                self.first_reply = result_text(await self.agent.run(max_steps=10))
            except Exception as e:
                self.first_reply = f"Browser shuru nahi ho saka: {e}"
            self.ready = True
        print(f"\nAgent: {self.first_reply}")

    async def page(self, request):
        return web.Response(text=CHAT_PAGE, content_type="text/html")

    async def status(self, request):
        return web.json_response({"ready": self.ready, "first_reply": self.first_reply})

    async def chat(self, request):
        message = (await request.json()).get("message", "").strip()
        if not message:
            return web.json_response({"reply": "Khaali message."})
        print(f"\nAap: {message}")
        async with self.lock:
            # Same agent, same browser: pichli baatein yaad rehti hain
            self.agent.add_new_task(f"{message}\n{CREDENTIALS_HINT}")
            try:
                reply = result_text(await self.agent.run(max_steps=25))
            except Exception as e:
                reply = f"Error: {e}"
        print(f"\nAgent: {reply}")
        return web.json_response({"reply": reply})


async def chat_with_browser(sensitive_data: dict | None = None):
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: API Key .env file mein nahi mili!")
        return

    llm = ChatGoogle(model=MAIN_MODEL, api_key=api_key)
    fallback_llm = ChatGoogle(model=FALLBACK_MODEL, api_key=api_key)

    browser = Browser(
        headless=False,           # browser screen par nazar aaye
        user_data_dir=PROFILE_DIR,
        keep_alive=True,          # har task ke baad browser khula rahe
    )

    # Pehla task: sirf page kholna. Baaki kaam chat box se.
    agent = Agent(
        task=f"Open {LOGIN_URL} and wait for the page to load. Report what is visible "
             f"(login form or trade room). Do not log in yet. {CREDENTIALS_HINT}",
        llm=llm,
        fallback_llm=fallback_llm,
        browser=browser,
        # LLM ko asli values nahi jaati, sirf placeholder names (x_email, x_password)
        sensitive_data=sensitive_data,
    )

    server = ChatServer(agent)
    app = web.Application()
    app.router.add_get("/", server.page)
    app.router.add_get("/status", server.status)
    app.router.add_post("/chat", server.chat)

    runner = web.AppRunner(app)
    await runner.setup()
    # Sirf is computer se khulega (127.0.0.1), network par nahi
    await web.TCPSite(runner, "127.0.0.1", CHAT_PORT).start()

    chat_url = f"http://127.0.0.1:{CHAT_PORT}"
    print(f"Model: {MAIN_MODEL} (fallback: {FALLBACK_MODEL})")
    print(f"Chat box: {chat_url}")
    print("Band karne ke liye is terminal mein Ctrl+C dabayein.")
    webbrowser.open(chat_url)

    try:
        await server.run_first_task()
        await asyncio.Event().wait()  # Ctrl+C tak chalta rahe
    finally:
        await runner.cleanup()
        await browser.kill()
        print("Browser band ho gaya.")


if __name__ == "__main__":
    # Credentials .env mein hain (IQ_EMAIL, IQ_PASSWORD)
    iq_email = os.getenv("IQ_EMAIL")
    iq_password = os.getenv("IQ_PASSWORD")
    if not iq_email or not iq_password:
        print("Error: IQ_EMAIL / IQ_PASSWORD .env file mein nahi mile!")
        raise SystemExit(1)

    try:
        asyncio.run(chat_with_browser(
            sensitive_data={"x_email": iq_email, "x_password": iq_password},
        ))
    except KeyboardInterrupt:
        pass
