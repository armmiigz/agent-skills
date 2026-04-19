---
name: evaluation-harness
description: Systematic evaluation of LLM applications. Build golden datasets, scoring rubrics, and regression reports to ensure model quality and catch regressions.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "llm evaluation"
    - "ai testing"
    - "model benchmarking"
    - "regression testing ai"
    - "eval harness"
---

# Evaluation Harness (AI Engineering)

## Core Principles
1. **Repeatability**: Tests must be deterministic and runnable in CI.
2. **Multiple Metrics**: Use a mix of exact match, semantic similarity, and LLM-as-judge.
3. **Regression Focus**: Always compare current results against a baseline.

## Workflow

### 1. Build a Golden Dataset
A "Golden Dataset" contains high-quality input-output pairs that represent ground truth.
```json
[
  {
    "id": "qa_01",
    "input": "How do I reset my password?",
    "expected_output": "Navigate to settings and click 'Forgot Password'.",
    "rubric": { "correctness": 1.0, "tone": 0.8 }
  }
]
```

### 2. Implement Scoring Rubrics
```python
def score_semantic(actual, expected):
    # Use cosine similarity of embeddings
    return cosine_similarity(get_embedding(actual), get_embedding(expected))

def score_llm_judge(actual, expected, criteria):
    # Prompt another LLM to grade the output based on criteria
    return llm.grade(actual, expected, criteria)
```

### 3. Run & Report
- **Execute**: Run the model against the full dataset.
- **Compare**: Generate a report showing regressions (cases that used to pass but now fail).
- **CI**: Fail the build if the pass rate drops below the defined threshold.

## Security & Ethics
- **Data Privacy**: Ensure golden datasets do not contain PII (Personally Identifiable Information).
- **Bias Monitoring**: Include test cases specifically designed to detect bias or toxicity.

## Gotchas
- **LLM Flakiness**: LLM judges can be inconsistent. Run them multiple times or use high temperature=0 to minimize variance.
- **Cost**: Semantic similarity and LLM judging can be expensive. Use cheaper models for evaluation if possible.
- **Overfitting**: Don't just optimize for the golden dataset; ensure it remains representative of real-world usage.

## Verification Checklist
- [ ] Golden dataset includes edge cases and failure modes.
- [ ] Baseline established for comparison.
- [ ] Scoring functions cover both accuracy and formatting.
- [ ] Regression report is automatically generated.
- [ ] CI integration blocks deployment on quality drop.
