# AI/BI Dashboards

## Run Order

| Step | What | Where |
|------|------|-------|
| 1 | Run `day5_01_dashboard_data_prep.py` | Databricks notebook |
| 2 | Build 5 dashboards in Databricks UI | Databricks Dashboards |
| 3 | Add widgets using SQL from `day5_02_dashboard_specs.py` | Databricks UI |

---

## The 5 Dashboards

### Dashboard 1 — Complaint Heatmap
**Question it answers:** Where are complaints concentrated?

| Widget | Type | What it shows |
|--------|------|---------------|
| Borough × Month Heatmap | Heatmap | Complaint density by location and time |
| Top 10 Complaint Types | Horizontal Bar | Most common issue types |
| Open Complaints | Counter | Live count of unresolved complaints |
| Complaint Volume Trend | Line | 6-month complaint volume by borough |

---

### Dashboard 2 — Ward-wise Trends
**Question it answers:** How is each borough trending?

| Widget | Type | What it shows |
|--------|------|---------------|
| Complaint Trend by Borough | Line | Month-over-month per borough |
| MoM Change | Bar (+/-) | Which boroughs are getting better/worse |
| Borough Summary | Table | Total, unresolved, avg days open |
| Complaint Share | Pie | Borough distribution this month |

---

### Dashboard 3 — SLA Analytics
**Question it answers:** Are we meeting our response commitments?

| Widget | Type | What it shows |
|--------|------|---------------|
| SLA Health Score | Counter | 0-100 score (100 = no breaches) |
| Total Breached | Counter | Absolute breach count |
| Breach Rate by Dept | Horizontal Bar | Which depts fail SLA most |
| Breach Trend | Line | SLA breach rate over time |
| Health by Dept × Severity | Heatmap | Where the worst SLA failures are |

---

### Dashboard 4 — Department Performance
**Question it answers:** Which departments are performing well?

| Widget | Type | What it shows |
|--------|------|---------------|
| Department Scorecard | Table | Resolution rate, escalation rate, severity |
| Tickets by Department | Stacked Bar | Volume and category breakdown |
| Resolution Rate vs Severity | Scatter | Efficiency vs difficulty trade-off |
| Field Visit Rate | Bar | Which depts need most site visits |

---

### Dashboard 5 — Escalation Insights
**Question it answers:** What's getting escalated and why?

| Widget | Type | What it shows |
|--------|------|---------------|
| Total Escalations | Counter | Overall escalation volume |
| Health Risk Escalations | Counter | Life/safety escalations |
| Resolved After Escalation | Counter | Escalation effectiveness % |
| Escalation Flow | Bar | From dept → to dept routing |
| Escalation Trend | Line | Volume over time by risk type |
| By Category | Horizontal Bar | Which complaint types escalate most |
| Recent Escalations | Table | Full detail of last 50 escalations |

---

## How to Build Each Dashboard in Databricks UI

1. Left sidebar → **Dashboards** → **New Dashboard**
2. Give it the name from the spec above
3. Click **Add widget** → **Visualization**
4. Paste the SQL from `day5_02_dashboard_specs.py` for that widget
5. Select chart type and map axes as specified
6. Click **Add filter** for any dropdown filters (borough, date range)
7. Drag widgets to arrange layout

---

## Recommended Filters to Add (All Dashboards)

| Filter | Type | Column |
|--------|------|--------|
| Date Range | Date picker | `period` or `month` |
| Borough | Multi-select | `borough` |
| Severity | Multi-select | `severity_score` |
| Department | Multi-select | `dept_code` |

---

## Tips

- **Refresh schedule:** Set each dashboard to refresh every 1 hour
  (Dashboard settings → Schedule refresh)
- **Share:** Dashboard → Share → add your team emails
- **Embed:** Each widget has an embed URL for external portals
- **AI Summary:** Click the ✨ button on any widget for an AI-generated
  text summary of what the chart shows

---

## Next: Day 6 — Databricks App Frontend
- Build the citizen-facing complaint submission UI
- Wire to the agent pipeline in real-time
- Show ticket status and AI analysis to citizens
