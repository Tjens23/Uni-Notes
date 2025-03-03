---
tags:
  - Notes
links: "[[Git Lecture 7 Common Issues]]"
creation date: 2024-11-10 21:14
modification date: Sunday 10th November 2024 21:14:15
semester: 3
year: 2024
---


---
# [[Git Lecture 7 Notes]]

---



### Common Git Problems and Solutions

- **Merge Conflicts**: Occur when Git is unable to automatically resolve differences in code between two commits. To resolve, manually edit the conflicting files to select the desired changes, then stage and commit them.
- **Detached HEAD State**: Happens when you check out a commit instead of a branch. To exit this state, checkout a branch (e.g., `git checkout main`) or create a new branch with your changes (`git checkout -b <new-branch>`).
- **Untracked Files**: Files not being tracked by Git can clutter the working directory. Use `git clean -f` to remove untracked files, or add them to `.gitignore` to keep them untracked.
- **Lost Commits**: If you accidentally delete a commit, use `git reflog` to find the lost commit's hash, then `git checkout <hash>` to recover it.

#### How to Undo Changes

- **Using `reset`**:
  - `git reset` is a powerful command used to undo changes by moving the current branch pointer to a previous commit, effectively rewinding the project history.
  - `git reset --soft <commit-hash>` moves the HEAD to the specified commit but keeps the working directory and staging area as they were.
  - `git reset --hard <commit-hash>` moves the HEAD to the specified commit and resets the staging area and working directory to match. **Warning:** this will discard uncommitted changes.

- **Using `revert`**:
  - `git revert <commit-hash>` creates a new commit that undoes the changes made in the specified commit. This is a safe way to undo changes and is preferable in shared/public repositories as it doesn't alter the project's history.

- **Using `checkout`**:
  - `git checkout <commit-hash> <file>` reverts the specified file to its state at the given commit. This can be used to undo changes in specific files without affecting the entire project.

### Troubleshooting

- Regularly commit and push your changes to avoid losing work.
- Use `git status` and `git log` frequently to monitor the state of your repository and the history of your changes.
- Be cautious with commands that can alter history (like `git reset --hard`), especially in shared repositories.
- Keep a backup of your repository if you plan to perform risky operations.