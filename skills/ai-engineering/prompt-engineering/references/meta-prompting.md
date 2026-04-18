# Meta-Prompting Techniques

Meta-prompting is the practice of using a "Generator" prompt to create "Target" prompts. This ensures consistency and high quality across diverse tasks.

## 1. The Generator Pattern
Use this meta-prompt to generate production-ready system prompts.

```markdown
# Role: Expert Prompt Engineer
# Task: Create a system prompt for an AI agent.
# Input: {{TASK_DESCRIPTION}}

# Instructions:
1. Define a clear 'Role' for the agent.
2. List specific 'Constraints' (e.g., no prose, JSON output).
3. Specify 'Input/Output' format.
4. Include a 'Error Handling' section.
5. Use imperative, token-efficient language.

# Output:
Return only the generated System Prompt.
```

## 2. The Multi-Persona Pattern (MoE)
Instead of one general prompt, break the task into personas.
- **Planner**: Outlines the steps.
- **Executor**: Performs the code/calculation.
- **Reviewer**: Checks for errors (The Critic).

## 3. Dynamic Few-Shot Injection
Instead of static examples, use a script to inject the most relevant examples from a `golden_dataset` based on semantic similarity (RAG for Prompts).

## 4. Constraint Hardening
Ensure the model cannot "break character" or ignore rules by using negative constraints and explicit boundary markers (e.g., `### END OF INSTRUCTIONS ###`).

## Token-Efficiency Checklist
- [ ] Are there redundant adjectives? (Remove them)
- [ ] Is the output format too verbose? (Use CSV or minified JSON)
- [ ] Can instructions be merged? (e.g., "Be polite and friendly" -> "Tone: Friendly")
