# 🔍 SonarQube Code Quality & Static Analysis Overview

SonarQube is the industry-standard platform for Continuous Code Inspection, performing automatic static code analysis to detect bugs, code smells, and security vulnerabilities across 30+ programming languages.

---

## 🎯 1. Static Analysis vs Dynamic Unit Testing

```mermaid
graph TD
    subgraph DYNAMIC["Dynamic Analysis (Unit Tests: mvn test)"]
        D1["Executes compiled code in JVM"]
        D2["Validates runtime behavior: Does method calculate total correctly?"]
        D3["Pass / Fail assertion outcomes"]
    end

    subgraph STATIC["Static Analysis (SonarQube)"]
        S1["Inspects code text & Abstract Syntax Tree (AST) WITHOUT running it"]
        S2["Detects security vulnerabilities (SQL injection, hardcoded tokens)"]
        S3["Detects architectural technical debt & duplicated lines"]
        S4["Enforces Quality Gate policy"]
    end
```

---

## 🔬 2. The Four Pillars of SonarQube Inspection

1. **Bugs:** Coding flaws that will likely cause crashes, memory leaks, or erratic runtime failures (e.g. NullPointerExceptions, unclosed I/O streams).
2. **Vulnerabilities:** Security flaws exposed to attackers (e.g. SQL Injection vulnerabilities, cross-site scripting [XSS], insecure cryptographic algorithms).
3. **Security Hotspots:** Sensitive pieces of code that require human architectural review (e.g. CSRF token validation, cookie configuration).
4. **Code Smells (Maintainability):** Sloppy, convoluted code that increases technical debt, making maintenance painful (e.g. dead code, duplicated blocks, functions with 15 arguments).

---

## ⚖️ 3. The SonarQube Architecture

```mermaid
flowchart TD
    SCANNER["SonarQube Scanner / Maven Plugin<br/>(Runs inside Jenkins Workspace)"]
    
    subgraph SONAR_SERVER["SonarQube Dedicated Server (EC2 :9000 / :80)"]
        WEB["SonarQube Web UI (Port 9000)<br/>Rendered via Nginx Proxy (:80)"]
        SEARCH["Embedded Elasticsearch<br/>(Index search, metrics, rules)"]
        CE["Compute Engine (Worker Thread)<br/>Processes uploaded analysis AST reports"]
        DB[("PostgreSQL Database<br/>(Stores historical quality data)")]
        
        WEB --- SEARCH
        WEB --- CE
        CE --- DB
        WEB --- DB
    end

    SCANNER -- "1. Uploads AST report via HTTP POST" --> WEB
    CE -- "2. Background worker calculates Quality Gate" --> CE
    CE -- "3. Webhook calls Jenkins with Pass/Fail" --> JENKINS["Jenkins Controller (:8080)"]
```
