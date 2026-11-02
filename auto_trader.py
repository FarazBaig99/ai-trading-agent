import time
import requests

API_BASE_URL = "http://127.0.0.1:8000"
SYMBOL = "BTC-USD"
TRADE_AMOUNT = 0.01  # Quantity jo trade karni hai

def run_trading_bot():
    print(f"Auto Trading Bot Shuru Ho Gaya Hai ({SYMBOL} ke liye)...\n")

    while True:
        try:
            # 1. API se signal maangein
            response = requests.get(f"{API_BASE_URL}/signal/{SYMBOL}")
            
            if response.status_code == 200:
                data = response.json()
                price = data["current_price"]
                rsi = data["rsi"]
                decision = data["decision"]
                reason = data["reason"]

                print(f"[CHECK] Price: ${price} | RSI: {rsi} | Decision: {decision}")
                print(f"        Reason: {reason}")

                # 2. Agar BUY ya SELL signal mile toh trade endpoint call karein
                if decision in ["BUY", "SELL"]:
                    print(f"\n🚨 {decision} SIGNAL MILA! Order bhej rahe hain...")
                    
                    order_payload = {
                        "symbol": SYMBOL,
                        "action": decision,
                        "amount": TRADE_AMOUNT
                    }
                    
                    order_response = requests.post(
                        f"{API_BASE_URL}/trade", 
                        json=order_payload
                    )
                    
                    if order_response.status_code == 200:
                        print("✅ Order Execute Ho Gaya:", order_response.json())
                    else:
                        print("❌ Order execute karne mein masla aaya:", order_response.text)

                else:
                    print("⏳ Market neutral hai, agle check tak intezar...")

            else:
                print("API se signal nahi mil saka:", response.status_code)

        except Exception as e:
            print("Error aaya:", str(e))

        # Har 60 seconds (1 minute) baad dobara check karein
        print("-" * 50)
        time.sleep(60)

if __name__ == "__main__":
    run_trading_bot()