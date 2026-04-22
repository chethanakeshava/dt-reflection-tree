graph TD
    %% Global Styling
    classDef startEnd fill:#1e1e1e,stroke:#333,stroke-width:2px,color:#fff;
    classDef question fill:#2b5c8f,stroke:#1e3f66,stroke-width:2px,color:#fff;
    classDef reflection fill:#2e7d32,stroke:#1b5e20,stroke-width:2px,color:#fff;
    classDef bridge fill:#6a1b9a,stroke:#4a148c,stroke-width:2px,color:#fff;
    classDef decision fill:#d84315,stroke:#bf360c,stroke-width:2px,color:#fff;
    classDef summary fill:#fbc02d,stroke:#f57f17,stroke-width:2px,color:#000;

    START([START]):::startEnd --> A0_OPEN[A0_OPEN: How did today feel?]:::question
    
    subgraph "Axis 1: Locus (Agency)"
        A0_OPEN -->|Drained / Energised| A1_Q1_HIGH[A1_Q1_HIGH]:::question
        A0_OPEN -->|Frustrated / Flat| A1_Q1_LOW[A1_Q1_LOW]:::question

        A1_Q1_HIGH -->|Prepared / Adapted| A1_Q2_INT[A1_Q2_INT]:::question
        A1_Q1_HIGH -->|Team / Luck| A1_Q2_EXT[A1_Q2_EXT]:::question
        
        A1_Q1_LOW -->|Looked for control| A1_Q2_INT
        A1_Q1_LOW -->|Waited / Pushed / Stuck| A1_Q2_EXT

        A1_Q2_INT --> A1_D2{Dominant Axis 1?}:::decision
        A1_Q2_EXT --> A1_D2
        
        A1_D2 -->|Internal| A1_R_INT[A1_R_INT: Driver's Seat]:::reflection
        A1_D2 -->|External| A1_R_EXT[A1_R_EXT: Outside Pull]:::reflection
    end

    A1_R_INT --> BRIDGE_1_2([BRIDGE 1->2]):::bridge
    A1_R_EXT --> BRIDGE_1_2

    subgraph "Axis 2: Orientation (Contribution vs Entitlement)"
        BRIDGE_1_2 --> A2_OPEN[A2_OPEN: Interactions?]:::question
        
        A2_OPEN -->|Helped / Useful| A2_Q1_CONTRIB[A2_Q1_CONTRIB]:::question
        A2_OPEN -->|Own work / Give > Get| A2_Q1_ENTITLE[A2_Q1_ENTITLE]:::question
        
        A2_Q1_CONTRIB --> A2_D1{Dominant Axis 2?}:::decision
        A2_Q1_ENTITLE --> A2_D1
        
        A2_D1 -->|Contribution| A2_Q2_CONTRIB[A2_Q2_CONTRIB]:::question
        A2_D1 -->|Entitlement| A2_Q2_ENTITLE[A2_Q2_ENTITLE]:::question
        
        A2_Q2_CONTRIB --> A2_R_CONTRIB[A2_R_CONTRIB: Oriented to giving]:::reflection
        A2_Q2_ENTITLE --> A2_R_ENTITLE[A2_R_ENTITLE: Attention on owed]:::reflection
    end

    A2_R_CONTRIB --> BRIDGE_2_3([BRIDGE 2->3]):::bridge
    A2_R_ENTITLE --> BRIDGE_2_3

    subgraph "Axis 3: Radius (Perspective)"
        BRIDGE_2_3 --> A3_OPEN[A3_OPEN: Biggest Challenge?]:::question
        
        A3_OPEN -->|Just me| A3_Q1_SELF[A3_Q1_SELF]:::question
        A3_OPEN -->|Team / Colleague / Customer| A3_Q1_WIDE[A3_Q1_WIDE]:::question
        
        A3_Q1_SELF --> A3_D3{Dominant Axis 3?}:::decision
        A3_Q1_WIDE --> A3_D3
        
        A3_D3 -->|Self| A3_Q2_SELF[A3_Q2_SELF]:::question
        A3_D3 -->|Wide| A3_Q2_WIDE[A3_Q2_WIDE]:::question
        
        A3_Q2_SELF --> A3_R_SELF[A3_R_SELF: Narrow frame]:::reflection
        A3_Q2_WIDE --> A3_R_WIDE[A3_R_WIDE: Others in frame]:::reflection
    end

    A3_R_SELF --> SUMMARY[[SUMMARY - Matrix Synthesis]]:::summary
    A3_R_WIDE --> SUMMARY
    
    SUMMARY --> END([END]):::startEnd
    