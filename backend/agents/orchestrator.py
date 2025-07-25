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
                    result = agent.analyze(resume_text, job_description)
                else:
                    result = agent.analyze(resume_text)
                # Ensure all agent results are dictionaries for frontend compatibility
                if hasattr(result, 'dict') and callable(result.dict):
                    return name, result.dict()
                if isinstance(result, dict):
                    return name, result
                # If result is a pydantic BaseModel, convert to dict
                try:
                    import pydantic
                    if isinstance(result, pydantic.BaseModel):
                        return name, result.dict()
                except ImportError:
                    pass
                return name, result
            except Exception:
                return name, 'ERROR'

        results = {}
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(agent_task, name, agent) for name, agent in self.agents.items()]
            for future in as_completed(futures):
                name, status = future.result()
                results[name] = status

        # --- Compute overall score ---
        weights = {
            'ats': 0.20,
            'projects': 0.25,
            'tailoring': 0.20,
            'skills': 0.15,
            'digital': 0.10,
            'content': 0.05,  # summary/objective
            'education': 0.05
        }
        total_score = 0.0
        total_weight = 0.0
        for key, weight in weights.items():
            agent_result = results.get(key)
            score = 0.0
            if isinstance(agent_result, dict) and 'score' in agent_result and isinstance(agent_result['score'], (int, float)):
                score = agent_result['score']
            total_score += score * weight
            total_weight += weight
        overall_score = round(total_score / total_weight, 2) if total_weight > 0 else 0.0

        # --- Aggregate feedback and suggestions ---
        all_feedback = []
        all_suggestions = []
        for key in weights.keys():
            agent_result = results.get(key)
            if isinstance(agent_result, dict):
                feedback = agent_result.get('feedback')
                if feedback:
                    if isinstance(feedback, list):
                        all_feedback.extend(feedback)
                    else:
                        all_feedback.append(str(feedback))
                suggestions = agent_result.get('suggestions')
                if suggestions:
                    if isinstance(suggestions, list):
                        all_suggestions.extend(suggestions)
                    else:
                        all_suggestions.append(str(suggestions))

        # --- Use LLM to synthesize overall feedback ---
        from .utils import get_gemini_overall_feedback
        try:
            overall_feedback = get_gemini_overall_feedback(all_feedback, all_suggestions)
        except Exception:
            # Fallback: simple aggregation
            overall_feedback = '\n'.join(all_feedback + all_suggestions)

        # --- Return results with overall score and feedback ---
        results['overall'] = {
            'score': overall_score,
            'feedback': overall_feedback
        }
        return results
