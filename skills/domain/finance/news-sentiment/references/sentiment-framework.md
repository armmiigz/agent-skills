# News Sentiment Framework

Framework for converting news into actionable investment intelligence.

## 1. Scoring Matrix
| Event Type | Sentiment Score | Typical Market Action |
|------------|-----------------|-----------------------|
| CEO Resignation (Unexpected) | -0.8 | Sell-off, increased volatility |
| Major Acquisition (Strategic) | +0.6 | Long-term growth signal |
| Regulatory Probe | -0.7 | Uncertainty, risk premium increase |
| Product Launch (Positive Reviews) | +0.4 | Short-term momentum |

## 2. Source Analysis (Yahoo/Google)
- **Sentiment Weighting**: News from primary sources (Reuters, Bloomberg) carries 2x weight over aggregated blogs.
- **Recency**: News older than 24 hours has a decay factor of 0.5. News older than 7 days is considered "Historical Context" and not "Current Sentiment".

## 3. Transmission Chain Mapping
When a news event occurs, analyze:
1. **Target**: The specific company.
2. **Competitors**: How does this give them an advantage or disadvantage?
3. **Supply Chain**: Are suppliers or distributors affected?
4. **Sector**: Is this a systemic issue for the whole industry?

## 4. Synthesis Pattern
Provide research in this format:
- **Headline**: [Summary]
- **Sentiment**: [Score]
- **Primary Impact**: [Stock/Sector]
- **Market Reaction Hypothesis**: [Expected movement]
