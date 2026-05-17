# Notebook 4: Genie Integration

**agentic-civic-resolution-app**

## Run Order

| Step | What | Where |
|------|------|-------|
| 1 | Run `day4_01_gold_tables.py` | Databricks notebook |
| 2 | Create Genie Space | Databricks UI |
| 3 | Add tables to Genie | Databricks UI |
| 4 | Paste instructions | Databricks UI |
| 5 | Add curated SQL queries | Databricks UI |
| 6 | Test example queries | Genie chat |

---

## Step 1 — Run Gold Tables Notebook
Run `day4_01_gold_tables.py` first. This creates 4 pre-aggregated tables
that make Genie faster and more accurate.

---

## Step 2 — Create Genie Space

Databricks UI → left sidebar → **Genie** → **Create Space**

```
Name:        CivicOps Analytics Assistant
Description: Conversational analytics for civic complaint governance.
             Ask about complaint trends, SLA breaches, department 
             performance, and chronic problem locations.
```

---

## Step 3 — Add Tables

Click **Add tables** and add:

```
civicops.silver.complaints
civicops.gold.processed_tickets
civicops.gold.complaints_by_borough_month
civicops.gold.dept_sla_performance
civicops.gold.complaint_type_trends
civicops.gold.severity_summary
civicops.memory.complaint_history
civicops.memory.recurring_complaints
civicops.memory.sla_status_history
civicops.memory.escalation_context
```

---

## Step 4 — Paste Instructions

Click **Instructions** tab → paste the full instructions block
from `day4_genie_setup.py` SECTION 1.

---

## Step 5 — Add Curated SQL Queries

Click **Curated queries** → **Add query** for each query in
`day4_genie_setup.py` SECTION 2. Use the comment above each
query as the Question text.

---

## Step 6 — Test These Queries

```
Which boroughs have the most unresolved complaints?
Why are sewage complaints increasing?
Which departments are breaching SLA the most?
What are the top chronic problem locations?
Show me critical complaints that are still open
What is the resolution rate by category?
Which complaints were escalated and why?
Show complaint trends for the last 6 months
Which departments have worst SLA compliance?
```

---

## Tips for Better Genie Answers

- **Be specific**: "How many OPEN Sanitation complaints in BROOKLYN this month?"
  works better than "show me complaints"
- **Use table names**: "From recurring_complaints, which locations are chronic?"
- **Ask follow-ups**: Genie remembers context within a session
- **Verify SQL**: Click "Show SQL" on any Genie answer to see what it generated

---
