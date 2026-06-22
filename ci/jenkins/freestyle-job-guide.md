# Jenkins Freestyle Job Guide

1. Create a New Item > **Freestyle project**.
2. Under **Source Code Management**, select Git and provide repo URL.
3. In **Build Environment**, select 'Provide Node & npm bin/ folder to PATH' or necessary JDK.
4. Add **Build Step** (e.g., Invoke top-level Maven targets: `clean package`).
5. Add **Post-build Action** to archive artifacts (`**/*.jar`).
