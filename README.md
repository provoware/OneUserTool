# OneUserTool

OneUserTool is a small PyQt-based application bundling several modules, such as
song lyric management, genre catalogues and a random generator. The project can
be launched with `python3 main.py` once the dependencies from
`requirements.txt` are installed.

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd OneUserTool
   ```
2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   python3 main.py
   ```

## Updating the repository

1. **Fetch updates** from the remote server and rebase your local changes:
   ```bash
   git pull --rebase
   ```
2. **Stage your modifications**
   ```bash
   git add <changed-files>
   ```
3. **Commit** with a concise message
   ```bash
   git commit -m "Describe your change"
   ```
4. **Push** your commit
   ```bash
   git push
   ```

## Tips for Git beginners

- Make regular commits so that each change set is small and meaningful.
- Use `git status` to see which files have changed and `git diff` to review
  modifications before committing.
- If you make a mistake, `git restore <file>` reverts changes in the working
  directory, while `git reset --soft HEAD~1` undoes the last commit (but keep
  your changes staged).
- Keep your branch up to date with `git pull --rebase` before pushing to avoid
  merge conflicts.

