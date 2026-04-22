# Design Rationale: The Daily Reflection Tree

## 1. Psychological Grounding
The objective of this reflection tree is to operationalize abstract psychological theories into a deterministic, navigable structure. Rather than relying on a black-box LLM to generate runtime advice, this tree encodes established behavioral science into a reliable state machine.

* **Axis 1: Locus of Control (Agency):** Grounded in Julian Rotter’s framework (1954), this axis differentiates between internal and external loci. The design deliberately avoids the terminology of "victim vs. victor," which can trigger defensive mechanisms. Instead, it measures *response latency*. Questions focus on the immediate reaction to friction: looking for leverage (internal locus) versus waiting for external resolution (external locus).
* **Axis 2: Orientation (Contribution vs. Entitlement):** Informed by Campbell’s concept of Psychological Entitlement (2004) and Organ’s Organizational Citizenship Behavior (1988). Entitlement is often an invisible cognitive bias to the person experiencing it. To measure this without moralizing, the questions isolate discretionary effort. It asks the user to weigh moments of unprompted contribution against feelings of unrecognized effort, effectively mapping their current transactional state within the organization.
* **Axis 3: Radius (Perspective):** Based on Maslow’s later work on Self-Transcendence (1969) and Batson’s empathy-as-understanding (2011). In predictive modeling, a wider context window generally yields better generalizations; similarly, human resilience scales with the radius of perspective. The questions gently test the boundaries of the user's awareness—whether they view challenges solely through the lens of their own workflow or as part of a broader system impacting colleagues and end-users.

## 2. Question Selection Strategy
The core challenge in designing the question nodes was preventing users from "gaming" the assessment to achieve a perceived high score. If questions simply ask "Are you a team player?", the resulting data becomes essentially useless noise. 

To solve this, the questions focus strictly on behavioral proxies rather than abstract feelings. For example, instead of asking "Do you take responsibility?", the tree asks, "When something went well today, what do you think made it happen?" The options force a choice between preparation (internal) and luck/team intervention (external). 

Furthermore, the questions are designed to meet a tired employee at the end of their day. The language is conversational and grounded in the reality of a workday workflow. It recognizes that feeling drained or frustrated is valid data, using those emotional states as the entry point to branch into the deeper structural questions.

## 3. Branching Design and Trade-offs
The tree functions as a directed acyclic graph (DAG) where user inputs trigger state updates (signals). 

**The Routing Logic:**
Instead of hardcoding every possible pathway into a combinatorial explosion of question nodes, the architecture utilizes hidden `decision` nodes. This separates the user interface (the question) from the routing logic. By evaluating the accumulated signals at these checkpoints, the tree dynamically selects the next appropriate reflection or question, maintaining a clean data structure.

**Trade-offs Made:**
1.  **Depth vs. Friction:** A significant trade-off was limiting the tree to three main axes. While human behavior is infinitely complex, a massive, highly-nested tree would suffer from immense drop-off rates. The design sacrifices edge-case granularity to ensure completion, relying on the sophisticated `SUMMARY` node to synthesize the overlapping signals into a nuanced final insight.
2.  **Determinism vs. Flexibility:** Enforcing strict determinism means the tree cannot react to nuance outside the fixed options. However, this is a feature, not a bug. By forcing the user into one of four distinct categories, the tree acts as a forcing function for clarity, ensuring the diagnostic output is auditable and consistent across the organization.

## 4. Future Improvements
With more time, the following enhancements would be integrated into the system:
* **State Persistence:** Currently, the tree evaluates a single isolated session. Future iterations would write these daily signals to a time-series database. This would allow the system to recognize longitudinal trends (e.g., "You've leaned external on your locus for three consecutive days") and adjust the opening questions accordingly.
* **Dynamic Role-Contextualization:** The questions are currently universally applicable. By passing user metadata into the tree's initialization state, the node options could dynamically swap out to reflect domain-specific scenarios (e.g., swapping general terms for specific engineering or management scenarios) without changing the underlying psychological logic.
* **Advanced Data Validation:** Implementing an automated testing pipeline to parse the structure, verifying that every node resolves to a valid `next` key, and programmatically proving that there are zero dead-ends or infinite loops in the deterministic pathways.