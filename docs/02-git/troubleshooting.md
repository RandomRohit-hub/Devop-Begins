# 🩺 Git Troubleshooting & Conflict Resolution

Common Git errors, edge cases, merge conflict resolution, and credential issues.

---

## 💥 1. Resolving Merge Conflicts

When two branches modify the same line in a file, Git pauses the merge:

```text
Auto-merging pom.xml
CONFLICT (content): Merge conflict in pom.xml
Automatic merge failed; fix conflicts and then commit the result.
```

### Conflict Markers Explained:
```xml
<<<<<<< HEAD (Current Branch)
    <version>2.3.0</version>
=======
    <version>2.4.0-SNAPSHOT</version>
>>>>>>> feature/new-version (Incoming Branch)
```

### Resolution Steps:
1. Open the conflicted file and decide which content to keep (or combine both).
2. Remove the conflict marker lines (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Stage the resolved file:
   ```bash
   git add pom.xml
   ```
4. Complete the merge:
   ```bash
   git commit -m "Merge branch 'feature/new-version': resolve version conflict"
   ```
5. If you want to abandon the merge completely:
   ```bash
   git merge --abort
   ```

---

## 🚨 2. Common Git Errors & Fixes

### Error A: `fatal: Authentication failed for 'https://github.com/...'`
* **Cause:** GitHub discontinued password authentication for Git operations.
* **Fix:** Use a GitHub **Personal Access Token (PAT)** or configure SSH keys (`ssh -T git@github.com`). In Jenkins, store the PAT in **Credentials** as *Secret text* or *Username with password*.

### Error B: `error: failed to push some refs to ...`
* **Cause:** The remote repository contains commits that do not exist locally.
* **Fix:** Pull remote changes before pushing:
  ```bash
  git pull --rebase origin main
  git push origin main
  ```

### Error C: Detached HEAD State
* **Symptom:** `You are in 'detached HEAD' state. You can look around, make experimental changes...`
* **Cause:** You checked out a specific commit hash rather than a branch name (`git checkout b2f9cdf`).
* **Fix:** Create a new branch pointing to this state:
  ```bash
  git switch -c recovery-branch
  ```
  Or return to your main branch:
  ```bash
  git switch main
  ```

### Error D: Accidentally Committed a Secret / Password
* **Immediate Fix:**
  1. Revoke the token/credential immediately on AWS / GitHub / Nexus.
  2. Remove file from git tracking without deleting it from disk:
     ```bash
     git rm --cached sensitive.pem
     echo "sensitive.pem" >> .gitignore
     git commit --amend -m "Remove sensitive credential"
     ```
  3. If already pushed, use `git filter-repo` or BFG Repo-Cleaner to scrub git history.
