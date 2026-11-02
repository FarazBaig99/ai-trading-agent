from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

app = FastAPI(title="My Trading AI Engine")

class TradeRequest(BaseModel):
    symbol: str
    action: str
    amount: float

@app.get("/")
def home():
    return {"message": "Trading AI Engine active hai!"}

@app.get("/price/{symbol}")
def get_real_price(symbol: str):
    try:
        ticker = yf.Ticker(symbol.upper())
        data = ticker.history(period="1d")
        if data.empty:
            raise HTTPException(status_code=404, detail="Symbol nahi mila!")
        
        current_price = data['Close'].iloc[-1]
        return {
            "symbol": symbol.upper(),
            "current_price": round(float(current_price), 2),
            "status": "live"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/signal/{symbol}")
def get_trade_signal(symbol: str):
    try:
        ticker = yf.Ticker(symbol.upper())
        # Pichle 1 mahine ka hourly data
        df = ticker.history(period="1mo", interval="1h")
        
        if df.empty or len(df) < 20:
            raise HTTPException(status_code=400, detail="Pura data nahi mil saka")

        # Indicators calculate karein
        rsi_series = RSIIndicator(close=df['Close'], window=14).rsi()
        sma_series = SMAIndicator(close=df['Close'], window=20).sma_indicator()
        
        latest_price = round(float(df['Close'].iloc[-1]), 2)
        latest_rsi = round(float(rsi_series.iloc[-1]), 2)
        latest_sma = round(float(sma_series.iloc[-1]), 2)

        # Strategy Decision Logic
        if latest_rsi < 35:
            decision = "BUY"
            reason = f"RSI {latest_rsi} par oversold zone mein hai (potential reversal)."
        elif latest_rsi > 65:
            decision = "SELL"
            reason = f"RSI {latest_rsi} par overbought zone mein hai (potential correction)."
        else:
            decision = "HOLD"
            reason = f"RSI {latest_rsi} neutral zone mein hai, clear breakout ka intezar karein."

        return {
            "symbol": symbol.upper(),
            "current_price": latest_price,
            "rsi": latest_rsi,
            "sma_20": latest_sma,
            "decision": decision,
            "reason": reason
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/trade")
def place_trade(order: TradeRequest):
    return {
        "status": "Order Placed Successfully",
        "action": order.action.upper(),
        "symbol": order.symbol.upper(),
        "amount": order.amount
    }