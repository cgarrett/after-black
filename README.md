# After Black

[Pre-commit](https://pre-commit.com) hook to identify where the Black formatter for python may have tried to put multiple
string fragments on the same line that need to be concatenated into one string.

This pre-commit hook should be run after the Black formatter pre-commit hook.

## Usage

```
  - repo: https://github.com/cgarrett/after-black
    rev: v0.0.2
    hooks:
      - id: after_black
```