import os

def optimize_prompt(target_prompt):
    """
    Demonstrates the Critic Loop logic.
    In a real scenario, this would call an LLM API (e.g., Claude or GPT-4).
    """
    critic_system_prompt = """
    You are a Prompt Optimizer. Your goal is to review the provided prompt for:
    1. Ambiguity (unclear instructions).
    2. Token waste (conversational fillers, redundant words).
    3. Missing constraints (output format, error handling).
    
    Output a 'CRITIQUE' and an 'OPTIMIZED_PROMPT'.
    Maintain maximum token-efficiency.
    """
    
    # Simulate LLM Response
    critique = "The prompt uses conversational fillers like 'I want you to' and lacks a strict output format."
    optimized_prompt = f"""
    # Role: [Derived from target]
    # Task: [Derived from target]
    # Constraints:
    - No conversational fillers.
    - Output: JSON only.
    - Token-efficient imperative language.
    
    Input Data: {{DATA}}
    """
    
    return {
        "original": target_prompt,
        "critique": critique,
        "optimized": optimized_prompt
    }

if __name__ == "__main__":
    example_prompt = "I want you to act as a financial advisor and please calculate the net worth of this person based on their assets and liabilities. Make it look nice."
    
    result = optimize_prompt(example_prompt)
    print("--- CRITIQUE ---")
    print(result["critique"])
    print("\n--- OPTIMIZED PROMPT ---")
    print(result["optimized"])
