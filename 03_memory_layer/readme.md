# memory layer
**agentic-civic-resolution-app**

## Run Order

| # | Notebook | What it does |
|---|----------|-------------|
| 1 | `day3_01_delta_memory_setup.py` | Creates `civicops.memory` schema + 4 Delta tables |
| 2 | `day3_02_memory_manager.py` | `CivicOpsMemory` class — all read/write operations |
| 3 | `day3_03_context_pipeline.py` | Context-aware orchestrator wired to memory |

---

## Memory Tables (Delta)

| Table | Key behaviour |
|-------|--------------|
| `civicops.memory.complaint_history` | Upserted on every `save_ticket()` call |
| `civicops.memory.recurring_complaints` | Auto-updated; `is_chronic=True` at 3+ occurrences |
| `civicops.memory.escalation_context` | Auto-written when `escalate=True` on any ticket |
| `civicops.memory.sla_status_history` | Written on every `update_status()` call |

---

## Key Behaviours

**Chronic detection** — 3rd complaint at same location/type flips `is_chronic=True` automatically.

**Severity boost** — `ContextAwareOrchestrator` bumps severity +1 for chronic locations, tightening SLA.

**SLA breach tracking** — `get_sla_breached()` returns all open tickets past deadline with `hrs_overdue`.

**No new infrastructure** — runs entirely on existing Delta/Unity Catalog. Swap to Lakebase later by replacing only `day3_02_memory_manager.py`.

---

## Upgrading to Lakebase Later

When Lakebase becomes available on your workspace:
1. Rewrite `day3_02_memory_manager.py` to use SQLAlchemy + psycopg2
2. Keep the same class name `CivicOpsMemory` and same method signatures
3. All downstream notebooks (`day3_03`, orchestrator, dashboards) work unchanged

---

