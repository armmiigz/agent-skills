---
name: system-design
description: Design scalable and reliable distributed systems. Covers architectural patterns (Microservices, Hexagonal, Event-driven), data modeling, API design, and infrastructure trade-offs.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Pure architectural planning"
  triggers:
    - "design system"
    - "architectural plan"
    - "scalable backend"
    - "database design"
    - "distributed system"
---

# System Design & Architecture

## Core Philosophy
1. **Trade-off Analysis**: Every design decision has pros and cons. Document the rationale.
2. **Scalability**: Design for 10x growth in data and traffic.
3. **Resilience**: Assume components will fail. Design for graceful degradation.

## 1. Design Patterns
- **Hexagonal Architecture**: Decouple business logic from external dependencies (DB, APIs).
- **Event-Driven**: Use message queues for asynchronous processing and decoupling.
- **Serverless/Edge**: Use edge computing for low-latency global delivery.

## 2. Data Strategy
- **SQL vs NoSQL**: Choose based on consistency requirements and data structure.
- **Caching**: Implement multi-layer caching (Browser, Edge, Server, DB).
- **Data Integrity**: Enforce constraints at the database level and use transactions where needed.

## 3. API Design
- **REST/GraphQL**: Choose based on consumer needs.
- **Versioning**: Plan for non-breaking changes from day one.
- **Rate Limiting**: Protect your services using [app-security](../../backend/security/SKILL.md).

## 4. Documentation (ADR)
Capture every major design decision in an [architecture-decision-record](../../foundation/architecture-decision-records/SKILL.md).

## Verification Checklist
- [ ] Design handles expected traffic/data growth.
- [ ] No single point of failure (High Availability).
- [ ] API is type-safe and documented.
- [ ] Security (Auth, Rate limiting) is integrated.
- [ ] Observability (Logging, Tracing) is planned.
