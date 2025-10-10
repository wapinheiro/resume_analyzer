import os
from vertexai.generative_models import GenerativeModel

def validate_agent_feedback(feedback, agent_name):
    """
    Uses Gemini LLM to validate if the feedback is a proper resume assessment.
    Returns True if valid, False otherwise.
    """
    prompt = f"""
You are a strict validator for resume analysis feedback from an agent named '{agent_name}'.
The feedback below should be a meaningful, relevant, and actionable assessment of a resume. It must NOT be:
- Instructions for the agent
- Meta-comments about what the agent should do
- Generic requirements or rules
- Off-topic or unrelated to the resume
- Hallucinations or AI disclaimers

Only accept feedback that is directly addressed to the resume owner, providing strengths, weaknesses, and suggestions for improvement.

Feedback to validate:
{feedback}

Is this feedback a valid, relevant resume assessment for the user? Reply ONLY with 'VALID' or 'INVALID' and a brief reason. Do not provide any other information.
"""
    model = GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    candidates = getattr(response, 'candidates', None)
    if candidates and len(candidates) > 0:
        content = getattr(candidates[0], 'content', None)
        if content and hasattr(content, 'parts') and len(content.parts) > 0:
            text = getattr(content.parts[0], 'text', None)
            if text:
                if 'INVALID' in text.upper():
                    return False
                if 'VALID' in text.upper():
                    return True
    return False
