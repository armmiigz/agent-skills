---
name: variance-analysis
description: Analyze discrepancies between planned and actual outcomes. Used for financial budgeting, project timelines, and performance tracking to identify root causes of deviations.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Data analysis logic"
  triggers:
    - "perform variance analysis"
    - "plan vs actual"
    - "budget deviation"
    - "analyze discrepancy"
    - "performance gap"
---

# Variance Analysis (Plan vs Actual)

## Core Philosophy
1. **Explain the "Why"**: Variance analysis is not just about the numbers; it's about identifying the events or decisions that caused the deviation.
2. **Actionable Insights**: Use the analysis to adjust future plans or take corrective action.
3. **Accuracy**: Ensure data sources are reliable before starting the analysis.

## 1. Analysis Types
- **Financial Variance**: Comparing Actual Spend/Revenue vs Budget.
- **Schedule Variance**: Comparing Actual Progress vs Project Roadmap.
- **Performance Variance**: Comparing Actual Metrics (e.g., LCP) vs Performance Budgets.

## 2. The Analysis Workflow
1. **Gather Data**: Collect planned values and actual results.
2. **Calculate Variance**: `Variance = Actual - Planned`.
3. **Identify Significance**: Focus on variances that exceed a certain threshold (e.g., >5% or >$1000).
4. **Determine Root Cause**: Interview stakeholders or analyze logs/data to find out why the deviation occurred.
5. **Report**: Summarize findings and suggest corrections.

## 3. Reporting Pattern
- **Favorable (F)**: Actual result is better than planned (e.g., higher revenue, lower cost).
- **Unfavorable (U)**: Actual result is worse than planned (e.g., higher cost, delayed timeline).

## Verification Checklist
- [ ] Variance is correctly calculated.
- [ ] Root causes are identified and explained.
- [ ] Analysis is objective and data-driven.
- [ ] Recommendations are actionable.
