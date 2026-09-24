# 🐙 Git Fundamentals & Core Concepts

Git is a distributed version control system (DVCS) designed to handle everything from small to very large projects with speed and efficiency.

---

## 🏛️ 1. Centralized vs Distributed Version Control

```mermaid
flowchart TD
    subgraph CVCS["Centralized (SVN, CVS)"]
        CS["Central Server"]
        U1["Developer 1"]
        U2["Developer 2"]
        U1 -- "Commit directly" --> CS
        U2 -- "Commit directly" --> CS
        NOTE1["Single point of failure.<br/>Cannot work offline."]
    end

    subgraph DVCS["Distributed (Git)"]
        REMOTE["Remote Origin (GitHub)"]
        R1["Local Repo 1<br/>(Full History)"]
        R2["Local Repo 2<br/>(Full History)"]
        R1 -- "Push / Pull" --> REMOTE
        R2 -- "Push / Pull" --> REMOTE
        NOTE2["Every clone is a full backup.<br/>Complete offline capability."]
    end
```

---

## 🏗️ 2. The 3 Areas of Git (Plus Remote)

Understanding Git requires understanding where your code resides at each stage:

```text
+---------------------+         +--------------------+         +--------------------+         +--------------------+
|  Working Directory  |         |   Staging Area     |         |  Local Repository  |         | Remote Repository  |
|  (Untracked / Edit) |         |      (Index)       |         |      (.git/)       |         |      (GitHub)      |
+---------------------+         +--------------------+         +--------------------+         +--------------------+
           │                               │                              │                              │
           │────────── git add ───────────>│                              │                              │
           │                               │───────── git commit ────────>│                              │
           │                               │                              │───────── git push ──────────>│
           │<────────────────────────────── git pull ────────────────────────────────────────────────────│
           │<──────────────────────── git checkout / restore ─────────────│                              │
```

1. **Working Directory:** Actual files on your local disk that you edit in VS Code or an IDE.
2. **Staging Area (Index):** A draft snapshot of changes being prepared for the next commit.
3. **Local Repository (`.git/`):** The permanent local database storing all committed snapshots and branch references.
4. **Remote Repository (GitHub):** The centralized cloud host enabling team collaboration and CI pipeline webhooks.

---

## 🔍 3. Git Internal Objects: Blobs, Trees, and Commits

Git is fundamentally a content-addressable filesystem:
* **Blob:** Stores raw file data (identified by SHA-1/SHA-256 hash).
* **Tree:** Represents a directory structure, mapping filenames to blob hashes.
* **Commit:** A pointer to a top-level root tree, containing metadata (author, timestamp, commit message, parent commit pointer).

```mermaid
graph TD
    COMMIT["Commit: b2f9cdf<br/>'Initial CI architecture'"] --> TREE["Tree: Root /"]
    TREE --> BLOB1["Blob: pom.xml"]
    TREE --> SUBTREE["Tree: src/"]
    SUBTREE --> BLOB2["Blob: App.java"]
```
