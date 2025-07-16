"""
ResumeAnalysisCrew: Orchestrates all specialized agents in parallel and aggregates their results.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from .ats_agent import ATSAgent
from .projects_agent import ProjectsAgent
from .skills_agent import SkillsAgent
from .tailoring_agent import TailoringAgent
from .digital_agent import DigitalAgent
from .content_agent import ContentAgent
from .education_agent import EducationAgent

class ResumeAnalysisCrew:
    def __init__(self):
        self.agents = {
            'ats': ATSAgent(),
            'projects': ProjectsAgent(),
            'skills': SkillsAgent(),
            'tailoring': TailoringAgent(),
            'digital': DigitalAgent(),
            'content': ContentAgent(),
            'education': EducationAgent(),
        }


    def run(self, resume_text: str, job_description: str = None):
        def agent_task(name, agent):
            try:
                if name == 'tailoring':
                    # Tailoring agent requires job_description
                    if not job_description:
                        return name, 'SKIPPED'
                    agent.analyze(resume_text, job_description)
                else:
                    agent.analyze(resume_text)
                return name, 'OK'
            except Exception:
                return name, 'ERROR'

        results = {}
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(agent_task, name, agent) for name, agent in self.agents.items()]
            for future in as_completed(futures):
                name, status = future.result()
                results[name] = status
        return results
