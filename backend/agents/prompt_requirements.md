# Shared LLM Prompt Requirements for All Agents

- Always respond with a single, valid JSON object. Do not include markdown, code blocks, or any text outside the JSON.
- The JSON must include the following keys: `score` (float, 0-10), `feedback` (list of strings), `suggestions` (list of strings), and `confidence` (float, 0-1).
- If you cannot provide a value, use a reasonable default (e.g., 0 or empty list).
- Do not include explanations, apologies, or any extra commentary outside the JSON object.
- Example response:
```json
{
  "score": 8.5,
  "feedback": ["Good section structure.", "Font is consistent."],
  "suggestions": ["Increase keyword density for ATS."],
  "confidence": 0.9
}
```

# Global Prompt Requirements for Resume Analyzer Agents

- Always respond with only a valid JSON object, no markdown, no code block, and no extra text or explanation.
- The JSON must match the required schema for the agent (see agent-specific requirements).
- Do not include any commentary, formatting, or explanation outside the JSON object.
- If you cannot complete the analysis, return a JSON object with an appropriate error message in the `feedback` field and set `confidence` to 0.0.
