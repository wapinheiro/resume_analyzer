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
