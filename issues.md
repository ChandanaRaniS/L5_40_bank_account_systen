
# Lab 5: Static Code Analysis — Issues and Fixes

## Objective
To identify and fix code quality, security, and formatting issues in the Bank Account System using Pylint, Bandit, and Flake8.

## Issues Identified and Fixed

| No. | Tool | Issue Identified | Fix Implemented |
|---|---|---|---|
| 1 | Pylint | Missing function docstrings | Added docstrings to functions |
| 2 | Pylint | Function name did not follow snake_case | Renamed createAccount to create_account |
| 3 | Pylint | Mutable default argument | Replaced transactions=[] with transactions=None |
| 4 | Pylint | Unused imports and variables | Removed unused imports and variables |
| 5 | Pylint | Broad exception handling | Added appropriate validation and error handling |
| 6 | Bandit | Unsafe use of eval() | Replaced expression evaluation with validated numeric input |
| 7 | Bandit | Weak MD5 hashing | Replaced MD5 with salted PBKDF2-HMAC-SHA256 |
| 8 | Bandit | Insecure random PIN generation | Used the secrets module |
| 9 | Bandit | Hard-coded secret token | Removed the hard-coded token |
| 10 | Bandit | Shell command execution | Removed os.system() and used normal file handling |
| 11 | Flake8 | Line exceeded the maximum length | Split the long statement across multiple lines |
| 12 | Flake8 | Formatting violations | Corrected formatting and whitespace |

## Before and After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.62/10 | 10.00/10 |
| Bandit | 6 potential issues | 0 reported issues |
| Flake8 | Multiple violations | No reported violations |

## Conclusion

Static code analysis helped improve the quality, security, readability, and maintainability of the Bank Account System. All three tools were rerun after the corrections. The final Pylint score was 10.00/10, Bandit reported no issues, and Flake8 reported no violations.
