# AGENTS.md

This is the single source of truth for project rules and instructions.

OpenCode loads this file automatically as its main instruction file. Do **not**
create `CLAUDE.md`, do not add Claude Code hooks, and do not depend on any Claude
Code runtime or configuration. This project targets OpenCode only.

## Project overview

- Name: `mailroom`
- Python: 3.12 or newer (pinned in `.python-version`)
- Environment and dependency manager: `uv`
- Layout: `src/` layout, package in `src/mailroom/`
- Tests: `tests/` with `pytest`
- Lint and format: `ruff`

## Commands

Always use `uv` so commands run against the project environment.

```bash
uv sync                 # create/update the environment from uv.lock
uv run mailroom         # run the CLI entry point
uv add <package>        # add a runtime dependency
uv add --dev <package>  # add a development dependency
uv run pytest           # run tests
uv run ruff check .     # lint
uv run ruff format .    # format
```

## Repository conventions

- Keep application code in `src/mailroom/` and tests in `tests/`.
- Keep dependency metadata in `pyproject.toml`; commit `uv.lock`.
- Do not commit `.venv/`, caches, build outputs, or secrets.
- Match the existing style; run tests and lint before finishing a task.

## How the owner learns (highest priority)

The owner learns by predicting before being told. Follow these rules exactly.

1. **Track reading progress.** Read `notes/reading-progress.md` before teaching
   anything. Update it whenever the owner reports reading a new section or
   document. Mark only what they have actually read as `read`.
2. **Only use read material.** When explaining or teaching, rely only on
   documents and sections marked `read`. Do not pull in unread material.
3. **Predict first.** Before introducing any concept, file, command, or code the
   owner has not read yet, ask them to predict what it does. Do not explain it,
   name its purpose, or reveal the answer before their prediction.
4. **Record the prediction.** Save the owner's prediction in the prediction log
   in `notes/reading-progress.md`.
5. **Then confirm or correct.** Only after they predict may you explain the
   concept and update the material's read status.
6. **Stay in scope.** Never jump ahead of what has been read, even if it would be
   convenient.

If a request cannot be fulfilled within what has been read, say so and offer to
introduce the next unread item through the predict-first flow.

## OpenCode configuration

- Use OpenCode-native features and configuration.
- `AGENTS.md` is the main instruction file; keep it current.
- Add skills, agents, plugins, or `opencode.json` only when the project actually
  needs them. Prefer the smallest native solution.
- Do not add Claude Code-specific files, hooks, or runtime dependencies.
