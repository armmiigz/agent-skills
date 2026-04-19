import argparse

def get_sentiment_label(score):
    if score >= 0.5: return "BULLISH"
    if score <= -0.5: return "BEARISH"
    return "NEUTRAL"

def analyze_headline(headline, keywords):
    # Simulated sentiment scoring logic
    score = 0.0
    
    # Very basic keyword mapping for demonstration
    positive = ['growth', 'profit', 'surpass', 'acquisition', 'buy', 'upgrade']
    negative = ['loss', 'decline', 'miss', 'probe', 'sell', 'downgrade']
    
    for word in headline.lower().split():
        if word in positive: score += 0.3
        if word in negative: score -= 0.3
        
    # Clamp score
    score = max(-1.0, min(1.0, score))
    return score

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate news sentiment analysis")
    parser.add_argument("--headline", required=True, help="News headline to analyze")
    
    args = parser.parse_args()
    score = analyze_headline(args.headline, [])
    label = get_sentiment_label(score)
    
    print(f"--- Sentiment Analysis ---")
    print(f"Headline: {args.headline}")
    print(f"Score: {score:.2f} ({label})")
    print(f"--------------------------")
