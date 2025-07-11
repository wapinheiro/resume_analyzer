# Agents Package

This directory is a Python package that contains the entire agent-based system for resume analysis, built using the CrewAI framework.

## Key Components:

-   `__init__.py`: Makes this directory a package.
-   `schemas.py`: Defines the Pydantic data models for standardized agent inputs and outputs.
-   `crew.py`: Orchestrates the agents and tasks, runs the analysis, and aggregates the final results.
-   `tasks.py`: Defines the specific analysis tasks assigned to each agent.
-   **Agent Files** (`ats_agent.py`, `projects_agent.py`, etc.): Each file defines a specialized agent with a unique role, goal, and backstory.
