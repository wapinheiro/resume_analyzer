import os
from vertexai.generative_models import GenerativeModel

def get_gemini_overall_feedback(feedback_list, suggestions_list):
    """
    Synthesizes overall resume feedback using Gemini LLM.
    Loads the prompt from 'overall_feedback_prompt.md' in the agents directory.
    """
    prompt_path = os.path.join(os.path.dirname(__file__), "overall_feedback_prompt.md")
    with open(prompt_path) as f:
        base_prompt = f.read()
    feedback_str = "\n- ".join([str(f) for f in feedback_list]) if feedback_list else "None"
    suggestions_str = "\n- ".join([str(s) for s in suggestions_list]) if suggestions_list else "None"
    full_prompt = f"{base_prompt}\n\nIndividual Agent Feedback:\n- {feedback_str}\n\nSuggestions:\n- {suggestions_str}\n\nPlease synthesize a concise, actionable overall feedback summary for the user."
    model = GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(full_prompt)
    # Extract plain text from Gemini response
    candidates = getattr(response, 'candidates', None)
    if candidates and len(candidates) > 0:
        content = getattr(candidates[0], 'content', None)
        if content and hasattr(content, 'parts') and len(content.parts) > 0:
            text = getattr(content.parts[0], 'text', None)
            if text:
                return text.strip()
    return str(response)
import json
import re
from .ats_agent import AgentResponse

def parse_gemini_llm_response(response) -> AgentResponse:
    """
    Extracts and parses the JSON analysis from Gemini model response.
    Returns an AgentResponse object.
    """
    try:
        # Vertex AI generative response: candidates[0].content.parts[0].text
        candidates = getattr(response, 'candidates', None)
        if candidates and len(candidates) > 0:
            content = getattr(candidates[0], 'content', None)
            if content and hasattr(content, 'parts') and len(content.parts) > 0:
                text = getattr(content.parts[0], 'text', None)
                if text:
                    # Try to extract JSON from code block or first {...}
                    code_block_match = re.search(r"```json(.*?)```", text, re.DOTALL)
                    json_str = None
                    if code_block_match:
                        json_str = code_block_match.group(1).strip()
                    else:
                        match = re.search(r"\{[\s\S]*?\}", text)
                        if match:
                            json_str = match.group(0)
                    if json_str:
                        try:
                            data = json.loads(json_str)
                            if isinstance(data, dict):
                                return AgentResponse(**data)
                        except Exception:
                            pass
    except Exception:
        pass
    # Fallback: return raw response for debugging
    return AgentResponse(
        score=0.0,
        feedback=[str(response)],
        suggestions=["Could not parse LLM response as JSON."],
        confidence=0.0
    )
