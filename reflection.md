
# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis is the process of examining source code without executing the program. It helps identify potential programming errors, security vulnerabilities, and coding-style violations before deployment.

## 2. What are the purposes of Pylint, Bandit, and Flake8?

Pylint checks code quality, naming conventions, missing documentation, and potential programming errors. Bandit identifies common security vulnerabilities in Python programs. Flake8 checks coding style, formatting, whitespace, and other PEP 8-related violations.

## 3. What issues were identified and how were they fixed?

The original Bank Account System contained unsafe expression evaluation using eval(), weak MD5 hashing, insecure PIN generation, a hard-coded token, shell command execution, a mutable default argument, and broad exception handling. These issues were addressed using validated numeric inputs, salted PBKDF2-HMAC-SHA256 hashing, the secrets module, safer file handling, and improved validation. Naming and formatting issues were also corrected.

## 4. What were the results after applying static analysis?

The original Pylint score was 5.62/10. After correcting the issues, the score improved to 10.00/10. Bandit initially identified six potential security issues and reported no issues after the fixes. Flake8 initially identified formatting and code-quality violations and reported no violations after correction.

## 5. What did you learn from this lab?

I learned that different static analysis tools identify different types of problems. Pylint improves code quality, Bandit helps identify security vulnerabilities, and Flake8 enforces consistent coding style. Using these tools together makes Python programs more readable, maintainable, and secure. Static analysis should also be combined with functional testing and code review.
