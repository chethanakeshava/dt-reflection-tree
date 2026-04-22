# DT Fellowship Assignment: The Daily Reflection Tree

This repository contains my submission for the DeepThought Growth Teams BA/DS Fellowship assignment. It features a deterministic, state-tracking decision tree designed to guide employees through a structured end-of-day reflection.

The tool measures psychological state across three axes—**Locus (Agency), Orientation (Contribution), and Radius (Perspective)**—without relying on any LLM at runtime. The intelligence is encoded directly into the data structure.

##  Repository Structure

```text
├── tree/
│   ├── reflection-tree.json       # Part A: The core data structure (deterministic tree)
│   └── tree-diagram.md            # Part A: Mermaid.js visual flowchart of the tree
├── agent/
│   └── agent.py                   # Part B: A lightweight Python CLI to execute the tree
├── transcripts/
│   ├── persona-1-transcript.md    # Part B: Sample run (Victim / Entitled / Self-centric)
│   └── persona-2-transcript.md    # Part B: Sample run (Victor / Contributing / Altrocentric)
├── write-up.md                    # Part A: Design rationale and psychological grounding
└── README.md                      # Documentation and instructions