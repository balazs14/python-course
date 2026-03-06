# NP5Course VS Code Workspace Profile

This project includes workspace-scoped VS Code configuration to reproduce the NP5Course setup without changing global settings.

## Included (project-scoped)

- `.vscode/settings.json` with NP5Course editor, Jupyter, Python, terminal, Git, and LaTeX behavior.
- `.vscode/extensions.json` with recommended extensions used in NP5Course.
- `.vscode/keybindings.NP5Course.json` as an optional keybindings template.

## Open This Folder Correctly

- Open the repository root as a VS Code folder.
- Accept extension recommendations when prompted.
- Create and activate the local `venv` from `README.txt`.

## Scope Limits in VS Code

Some VS Code behavior is profile/user-scoped by design and cannot be enforced per project:

- custom keybindings (`keybindings.json`)
- profile-only metadata
- machine-specific paths

This repository intentionally avoids machine-specific paths so it remains distributable.

If you want NP5-style keyboard behavior, copy entries from `.vscode/keybindings.NP5Course.json` into your User keybindings.
