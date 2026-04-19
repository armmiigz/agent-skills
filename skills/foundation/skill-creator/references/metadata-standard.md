# Skill Metadata Standard

This document defines the extended metadata standard for the **Agent Skills** repository.

## 1. Triggers
Triggers are keywords or phrases used by AI agents and CLI tools (like `npx skills`) for **Semantic Indexing**.
- **Purpose**: Helps the agent activate the correct skill without reading the entire repository.
- **Best Practice**: Use 5-8 descriptive phrases that represent user intent.
- **Example**:
  ```yaml
  triggers:
    - "setup auth"
    - "configure better-auth"
    - "api security"
  ```

## 2. Security Assessment
A human-readable declaration of the skill's risks and permissions.
- **Purpose**: Transparency and safety gating. Helps the agent warn the user before high-impact actions.
- **Levels**:
  - **Low**: Logic only, local file modification.
  - **Medium**: Runs scripts, modifies root config, or creates build pipelines.
  - **High**: Modifies Auth, handles PII, or makes external network requests.
- **Example**:
  ```yaml
  security_assessment:
    - "Risk: Medium"
    - "Permissions: File read/write"
    - "Execution: Runs bash scripts for setup"
  ```

## 3. Versioning
Standard Semantic Versioning (SemVer) or Simple Versioning.
- **Purpose**: Tracking updates and compatibility.
- **Standard**: Start with `"1.0"`. Increment minor for new features/references, major for breaking workflow changes.
