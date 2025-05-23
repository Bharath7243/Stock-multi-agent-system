# Multi-Agent Stock Analysis System

This project is built using modular agents via Google ADK architecture for analyzing stock data based on user queries.

## Agents

- **identify_ticker**: Identifies stock ticker from query
- **ticker_news**: Gets recent news about the stock
- **ticker_price**: Fetches the current stock price
- **ticker_price_change**: Calculates price change over a period
- **ticker_analysis**: Summarizes the reason behind stock movements

## Setup

1. Clone this repo
2. Install dependencies (`requests`, etc.)
3. Set your API keys for Alpha Vantage and others
4. Run `main.py` to test with sample queries

## Sample Query

```
Why did Tesla stock drop today?
```

## Output

```json
{
  "ticker": "TSLA",
  "news": "...",
  "price": "...",
  "price_change": "...",
  "analysis": "..."
}
```
