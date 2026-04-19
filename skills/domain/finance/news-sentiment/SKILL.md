---
name: news-sentiment-analysis
description: Analyze financial news from Yahoo/Google Finance. Covers real-time sentiment scoring (-1.0 to 1.0), market impact mapping, and sector-wide trend analysis.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Data analysis logic"
    - "Note: Requires external tools/plugins for real-time news fetching"
  triggers:
    - "analyze stock news"
    - "market sentiment"
    - "news impact assessment"
    - "yahoo finance news"
    - "google finance trends"
---

# News Sentiment Analysis

## Core Philosophy
1. **Signal over Noise**: Filter out generic reports; focus on market-moving events (Earnings, M&A, Macro shifts).
2. **Quantified Sentiment**: Convert qualitative news into quantitative scores for objective analysis.
3. **Transmission Chain**: Identify not just the direct impact, but the secondary effects across the supply chain/sector.

## 1. News Sources (Focus: Global)
- **Yahoo Finance**: Best for ticker-specific news, historical sentiment, and analyst comments.
- **Google Finance**: Best for tracking macro trends, regional news, and search-based sentiment.
- **Top Tiers**: Integrate insights from Reuters, Bloomberg, and CNBC via search tools.

## 2. Sentiment Scoring Framework
Score range: **-1.0 (Very Bearish)** to **+1.0 (Very Bullish)**.
- **Positive (+0.5 to +1.0)**: Upward earnings revisions, major product launches, favorable macro data.
- **Neutral (-0.4 to +0.4)**: In-line results, common market noise.
- **Negative (-1.0 to -0.5)**: Regulatory fines, security breaches, downward guidance, sector downturns.

## 3. Market Impact Mapping
- **Direct**: Impact on the specific stock ticker.
- **Indirect**: Impact on competitors (e.g., AAPL news affecting Samsung).
- **Macro**: Impact on the broader market or currency.

## Verification Checklist
- [ ] News is summarized with a clear sentiment score.
- [ ] Direct and indirect impacts are identified.
- [ ] Analysis avoids "Chinese Market" focus unless explicitly requested.
- [ ] Sources are cited and cross-referenced.
- [ ] Recommendation is provided based on the sentiment shift.
