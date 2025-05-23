"""
Main orchestrator for stock analysis multi-agent system
"""

from agents.identify_ticker.main import handle as identify_ticker
from agents.ticker_news.main import handle as ticker_news
from agents.ticker_price.main import handle as ticker_price
from agents.ticker_price_change.main import handle as ticker_price_change
from agents.ticker_analysis.main import handle as ticker_analysis

def process_query(query):
    ticker = identify_ticker(query)
    news = ticker_news(ticker)
    price = ticker_price(ticker)
    change = ticker_price_change(ticker)
    analysis = ticker_analysis({"news": news, "price_change": change})
    return {
        "ticker": ticker,
        "news": news,
        "price": price,
        "price_change": change,
        "analysis": analysis
    }

if __name__ == "__main__":
    example_query = "Why did Tesla stock drop today?"
    result = process_query(example_query)
    print(result)
