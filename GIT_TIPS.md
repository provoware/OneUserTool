# Git Guide for Beginners

This short document provides a few practical hints for working with Git if you
are new to the tool.

## Checking your work

- `git status` shows which files are modified, added or deleted in comparison to
the last commit.
- `git diff` displays the actual changes line by line. Use it before committing
  to double-check your edits.

## Undoing mistakes

- `git restore <file>` brings a file back to the state of the last commit.
- `git reset --soft HEAD~1` undoes the most recent commit while leaving your
  changes staged.
- `git reset --hard` should be used carefully; it discards all local changes.

## Learning more

The official Git documentation at <https://git-scm.com/doc> contains a thorough
book and quick-reference guides that are helpful once you become comfortable
with the basics.
