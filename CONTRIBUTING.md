# Contributing to the Resume Analyzer

This document outlines the development process for the Resume Analyzer project. We follow an "Always Running" approach to ensure stability, testability, and incremental progress.

## The "Always Running" Development Methodology

The core principle of this methodology is to build and test the application in small, incremental, and isolated steps. At each stage, we must have a working, testable piece of the application. This prevents complex, hard-to-debug integration errors and ensures that every component is solid before being combined.

### Development Steps

The process is strictly bottom-up, starting from the core external dependencies and moving up to the final user-facing application.

1.  **Test Core Dependencies First**: Before writing any application code, we ensure we can connect to and interact with core external services.
    *   **Example**: The first step is to create a simple, standalone Python script that connects to the Google Gemini/Vertex AI API and successfully receives a response. This script will have its own minimal set of dependencies.

2.  **Build and Test Components Incrementally**: Each new piece of functionality (e.g., an agent, a utility function) is built and tested in isolation.
    *   **Example**: Create a basic "ATS Agent" with a placeholder function that returns a simple string. Write a test script that imports this agent and verifies its output.

3.  **Accumulate and Test Integrations**: Once two or more components have been tested in isolation, they are integrated and tested *together*.
    *   **Example**: After the Gemini connection and a basic agent are working independently, we modify the agent to call the Gemini API. A new test is written to validate this combined functionality.

4.  **Continue Until End-to-End**: This process of building, testing, and integrating is continued until all components are assembled and the full end-to-end functionality is achieved (e.g., from the FastAPI endpoint to the AI agents and back).

5.  **Dockerize Last**: Only when the entire application is working and tested locally do we proceed to containerize it using Docker. This separates application debugging from containerization debugging.

By following this process, we ensure that the application is "always running" at some level of completion, making development a predictable and stable process.
