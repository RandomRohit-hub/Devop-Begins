# ⌨️ Essential Git Commands Reference

A practical cheat sheet covering everyday Git workflows, configuration, staging, committing, and remote synchronization.

---

## ⚙️ 1. Global Setup & Identity

```bash
# Configure identity (recorded in commit metadata)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name for new repositories
git config --global init.defaultBranch main

# View active configurations
git config --list
```

---

## 📝 2. Staging & Committing

```bash
# Check working tree status (untracked, modified, staged files)
git status

# Stage all changes in current repository
git add .

# Stage a specific file
git add pom.xml

# View un-staged line-by-line differences
git diff

# View differences that have been staged
git diff --staged

# Commit staged changes with descriptive message
git commit -m "Add SonarQube integration and quality gate step"

# Amend the most recent commit (e.g. fix typo in message or add missed file)
git commit --amend -m "Update commit message"
```

---

## 📜 3. Commit History & Inspection

```bash
# Display concise single-line commit history
git log --oneline

# Display commit graph showing branches and merges
git log --oneline --graph --decorate --all

# View the last N commits
git log -n 5 --stat

# Inspect a specific commit and its file diffs
git show b2f9cdf
```

---

## ☁️ 4. Remote Operations (Push, Pull, Fetch)

```bash
# List configured remote repositories and URLs
git remote -v

# Add a remote origin
git remote add origin https://github.com/RandomRohit-hub/Devop-Begins.git

# Fetch remote branches and tags without merging
git fetch origin

# Fetch and merge changes from remote tracking branch into local branch
git pull origin main

# Push new local branch and set upstream tracking
git push -u origin Continuous-Integration-and-Delivery-with-Jenkins

# Force push safely (verifies remote hasn't moved before overwriting)
git push --force-with-lease origin feature-branch
```

---

## 🧹 5. Discarding Changes & Stashing

```bash
# Discard unstaged modifications in a file (restore working directory copy)
git restore README.md

# Unstage a file from the staging area back to working directory
git restore --staged README.md

# Stash current uncommitted work to switch branches cleanly
git stash save "Work in progress on Jenkinsfile"

# List stored stashes
git stash list

# Re-apply the most recently stashed changes and remove from stash list
git stash pop
```
