# Project Coding and Documentation Standards

## 1. Overview

This document establishes the coding standards, documentation guidelines, and best practices for the **Resume Analyzer** project. Adhering to these standards is crucial for maintaining code quality, ensuring consistency, and facilitating collaboration among current and future contributors.

---

## 2. General Principles

- **Clarity over cleverness**: Write code that is easy to understand.
- **Consistency**: Strive for a uniform style across the entire codebase.
- **Document decisions**: Explain "why" something was done, not just "what" was done.
- **Automate everything**: Use linters, formatters, and scripts to enforce standards and streamline development.
- **Student-Focused**: Remember that this project will be maintained by students. Prioritize simplicity and clear documentation.

---

## 3. Project Structure and Documentation

### 3.1. Directory Structure

- Every major directory (e.g., `backend`, `frontend`, `scripts`, `backend/agents`) **must** contain a `README.md` file.
- The README should briefly explain the purpose of the directory and its contents.

### 3.2. Documentation Best Practices

- **`README.md` (Root)**: The main entry point. Should contain a project overview, tech stack, and setup instructions.
- **`docs/` Directory**: The central hub for all detailed documentation (Architecture, Roadmap, Cost Analysis, etc.).
- **Keep Docs Updated**: All documentation must be treated as a living document and updated alongside code changes.
- **Diagrams**: Use ASCII diagrams or Mermaid charts within markdown for architectural visualization.

---

## 4. Python (Backend) Best Practices

We will follow **PEP 8** as the primary style guide.

### 4.1. Code Structure and Organization

#### File Header
Every Python script (`.py`) should begin with a docstring header:
```python
"""
File: [filename.py]
Author: [Author Name/Team]
Date: [Creation Date]
Last Modified: [Date]

Purpose:
    A brief, one-sentence description of the file's purpose.

Dependencies:
    - crewai
    - fastapi
    - pydantic
"""
```

#### Import Order
Imports should be grouped in the following order:
1.  Standard library imports (`os`, `json`, `datetime`)
2.  Third-party imports (`fastapi`, `crewai`, `pydantic`)
3.  Local application imports (`from . import schemas`)

### 4.2. Naming Conventions

- **Modules/Files**: `snake_case.py` (e.g., `ats_agent.py`)
- **Classes**: `PascalCase` (e.g., `ResumeAnalysisTasks`)
- **Functions/Methods/Variables**: `snake_case` (e.g., `run_resume_analysis`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `ATS_AGENT_WEIGHT`)
- **Private Members**: `_leading_underscore`

### 4.3. Function and Method Design

- **Docstrings**: All public functions and methods must have a Google-style docstring.
  ```python
  def my_function(param1: str, param2: int = 0) -> bool:
      """Does something interesting.

      Args:
          param1: Description of the first parameter.
          param2: Description of the second parameter. Defaults to 0.

      Returns:
          A boolean indicating success or failure.
      
      Raises:
          ValueError: If param1 is invalid.
      """
      # ... implementation ...
  ```
- **Single Responsibility**: Functions should do one thing and do it well.
- **Type Hinting**: Use type hints for all function signatures.

### 4.4. Error Handling

- Use specific exceptions (`ValueError`, `FileNotFoundError`) instead of generic `Exception`.
- Provide clear, informative error messages in FastAPI responses.

### 4.5. FastAPI Specifics

- **Pydantic Models**: Define clear Pydantic models for all API request and response bodies to ensure data validation.
- **Dependency Injection**: Use FastAPI's dependency injection system for managing resources like LLM clients or database connections.
- **Async Operations**: Use `async` and `await` for all I/O-bound operations to keep the server non-blocking.

---

## 5. JavaScript/React (Frontend) Best Practices

We will follow the [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript) as a baseline.

### 5.1. Component Structure

- **File Naming**: Use `PascalCase` for component files (e.g., `ResumeUploader.js`).
- **Functional Components**: Prefer functional components with Hooks over class-based components.
- **Component-Based Styling**: Use CSS Modules or a CSS-in-JS library to scope styles to components. For this project, we will use **Tailwind CSS** utility classes primarily.

### 5.2. Naming Conventions

- **Variables/Functions**: `camelCase`
- **Components**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`

### 5.3. State Management

- For simple state, use `useState` and `useReducer`.
- For complex global state, consider `useContext` or a state management library like Zustand or Redux Toolkit if the app grows.

### 5.4. Comments

- Use comments to explain complex logic, business rules, or workarounds.
- Remove commented-out code before committing.

---

## 6. Code Review Checklist

Before merging any code, ensure the following:

- [ ] Code adheres to the standards in this document.
- [ ] All new functions and components are documented.
- [ ] Related project documentation (e.g., `ARCHITECTURE.md`) is updated.
- [ ] Code is formatted using an automated tool (e.g., Black for Python, Prettier for JS).
- [ ] All new code is self-documenting and easy to understand.
- [ ] No sensitive information (API keys, secrets) is hardcoded. Use environment variables.
