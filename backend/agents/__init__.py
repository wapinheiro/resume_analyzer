"""
File: __init__.py
Author: Wagner Pinheiro
Date: 2025-07-11
Last Modified: 2025-07-11

Purpose:
    This file makes the 'agents' directory a Python package, allowing for modular
    imports of agents, tasks, and schemas across the backend application.

Dependencies:
    - None
"""

# This file makes the 'agents' directory a Python package.
# You can optionally define package-level variables or import modules here.

# Example of pre-importing agents for easier access from other modules
# from .ats_agent import ats_agent
# from .projects_agent import projects_agent
# from .skills_agent import skills_agent
# from .tailoring_agent import tailoring_agent
# from .digital_presence_agent import digital_presence_agent
# from .content_quality_agent import content_quality_agent
# from .education_agent import education_agent
# from .crew import run_resume_analysis

__all__ = [
    "run_resume_analysis",
]
