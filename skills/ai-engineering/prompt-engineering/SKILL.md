---
name: prompt-engineering
description: Workflows to write, debug, and optimize prompts for LLMs. Includes few-shot selection, chain-of-thought structuring, system prompt design, and template composition.
metadata:
  version: "1.0"
  triggers:
    - "write prompt"
    - "improve prompt"
    - "few-shot examples"
    - "chain of thought"
    - "system prompt design"
    - "prompt template"
---

# Prompt Engineering & Optimization

## 1. Prompt Refinement Loop (Critic Loop)
Before deploying, use a stronger model to critique the prompt.
- **Workflow**: 
  1. Draft `Prompt_V1`.
  2. Ask Critic: "Review this prompt for ambiguity, token waste, and missing constraints."
  3. Apply feedback to create `Prompt_V2`.
  4. Benchmark `Prompt_V2` using [evaluation-harness](../evaluation-harness/SKILL.md).

## 2. Meta-Prompting (Prompt Generators)
Use structured templates to generate high-quality prompts dynamically.
- **Goal**: Standardize inputs/outputs across different model versions.
- **Technique**: Define a "Meta-Prompt" that accepts a `Task_Description` and outputs a production-ready `System_Prompt`.

## 3. Token-Efficiency Rules
- **Directness**: Use imperative verbs ("Calculate", "Refactor") instead of conversational fillers ("I would like you to...").
- **Variable Injection**: Use `{{VARIABLE_NAME}}` syntax for dynamic data.
- **Compression**: Remove redundant adjectives and repetitive instructions. Use bullet points.
- **Format Control**: Specify exact output schema (e.g., `JSON only, no prose`) to avoid wasteful token generation.

## 4. Advanced Patterns
- **Few-Shot Selection**: Use [few-shot-patterns](./references/few-shot-patterns.md). Limit to 3-5 diverse examples.
- **Chain-of-Thought**: Use [cot-patterns](./references/cot-patterns.md). Use only for complex reasoning to save tokens.
- **System Prompting**: Establish clear roles and safety boundaries using [system-prompt-design](./references/system-prompt-design.md).

## Gotchas
- **Ambiguity**: Vague terms like "Better" or "Quality" waste tokens. Use metrics or specific constraints.
- **Model Drift**: A prompt optimized for one model version may need re-optimization for the next.

## Verification Checklist
- [ ] Prompt uses imperative language (no fillers).
- [ ] Output format is strictly defined (e.g., JSON schema).
- [ ] Critic loop has been performed for production prompts.
- [ ] Token count is minimized while retaining all constraints.
- [ ] Few-shot examples (if any) are representative and concise.
