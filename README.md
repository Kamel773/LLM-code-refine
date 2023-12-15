# Can LLMs Patch Security Issues?

_With , Feedback-Driven Security Patching (FDSP), LLMs can generate potential solutions to fix security issues in code by receiving feedback from static code analysis._

![Example Image](https://github.com/Kamel773/LLM-code-refine/blob/main/workflows.png)

**Overview of our approach:** Initially, the model generates code. This code is subsequently analyzed for
security vulnerabilities using Bandit, a tool for static code analysis, to determine if there are any security issues.
Following this, feedback on any identified issues is incorporated into the model to generate possible solutions for
resolving the security issues. Finally, each proposed solution is sent back to the model for code refinement.
