# AGENTS.md

## Overview

Early-stage Python project managed with **uv**. Python 3.13 required (`.python-version`).

## Setup

```sh
uv sync          # install/lock dependencies
```

## Run

```sh
uv run python main.py
```

## Key facts

- Entry point: `main.py` (currently empty).
- Dependencies: `jupyterlab`, `pandas` (no Flask despite repo name).
- Package manager: **uv** (`pyproject.toml` + `uv.lock`). Do not use pip directly.
- No linter, formatter, typecheck, or test runner configured yet.
- `index.html` exists but is currently empty.
