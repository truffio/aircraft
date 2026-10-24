# Aeronef Project — Knowledge Base

The Aeronef project is a controlled systems-engineering experiment using AI to design, test, and reverse engineer a fictional flying vehicle, the Aeronef. The vehicle is deliberately simplified: a "Tic Tac"-shaped craft with six independent degrees of freedom, driven by fictional force emitters and operated primarily through autoflight.

The project has three principal objectives:

1. **Design** the Aeronef and its flight-control and autoflight systems.
2. **Build** a scalable simulation and automated verification environment.
3. **Reverse engineer** the resulting system from operational documentation and observable behavior, without access to its original design.

This repository holds the project's engineering documentation.

## Documents

| Document | Description |
| --- | --- |
| [OBJECTIVES.md](OBJECTIVES.md) | Project purpose, the three principal objectives, systems-engineering approach, and overall success criteria (L0). |
| [AIRCRAFT_CHARACTERISTICS.md](AIRCRAFT_CHARACTERISTICS.md) | Preliminary vehicle concept: motion and physics, force effectors, mass and fuel, flight controls, autoflight, and modeling boundaries. |
| [TESTING_ENVIRONMENT.md](TESTING_ENVIRONMENT.md) | Simulation core, interactive and automated testing, parallel execution, comparative evaluation, data collection, and traceability. |
| [REVERSE_ENGINEERING.md](REVERSE_ENGINEERING.md) | Information separation, material available to reverse-engineering agents, approach, assessment of results, and experimental integrity. |
| [METHODOLOGY.md](METHODOLOGY.md) | Requirements engineering methodology: level-by-level process, functional analysis, decomposition, writing rules (EARS, INCOSE), attributes, verification, traceability, and peer review. Hazard and failure analysis is deferred for now. |

## Status

All documents are initial concept summaries (October 2026). Detailed requirements, design, and procedures will be developed through a hierarchical, requirements-driven process (L0 → L1 → lower levels) with traceability and peer review.

## Information separation

This repository contains protected design information. Reverse-engineering agents must not be given access to it; see [REVERSE_ENGINEERING.md](REVERSE_ENGINEERING.md), section 7.
