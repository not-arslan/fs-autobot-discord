import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_trade_idea(symbol):
    prompt = f"""
    Give a trading analysis for {symbol.upper()}.
    Include:
    - Sentiment (Bullish/Bearish/Neutral)
    - Technical reasoning (RSI, EMA, MACD etc.)
    - Suggested Entry, SL, Target
    - Confidence %
    - Keep response under 150 words.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ GPT Error: {e}"
