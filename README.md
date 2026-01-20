# regime-stat-lab
### Engineering statistical edge through cross-asset regime intelligence.

#### Executive Summary
This project is an automated research environment designed to translate raw market volatility into actionable regime signals. By integrating cross-asset data streams (Equities, Crypto, Metals, FX), the system identifies shifts in market persistence and complexity using Hurst Exponents and Entropy metrics.

The objective is to replace "static" analysis with a dynamic ELT pipeline that ensures data sovereignty and mathematical integrity.
____
#### core objectives

* **Data Integrity:** Implements a "Calendar-Aware" validation layer to catch silent API omissions.
* **Regime Intelligence:** Calculates Hurst Exponent and Entropy to identify tradable market states.
* **Architecture-First:** Built on a containerized ELT stack for scalability and logic portability.

#### technical stack
Choosing an ELT approach over custom scripts ensures **idempotency** and allows for retroactive logic changes without data loss.
* **Orchestration:** Airbyte (Open Source) via OrbStack.
* **Storage:** Google BigQuery.
* **Transformation:** dbt (modeling for statistical persistence).
* **Analysis:** Evidence.dev for code-driven reporting.
