# CI Flow Diagram

Developer
    |
    v
GitHub Repository
    |
    v
Jenkins
    |
    +--> Checkout Code
    |
    +--> Build (Maven)
    |
    +--> Unit Test
    |
    +--> Checkstyle
    |
    +--> SonarQube Analysis
    |
    +--> Package Artifact
    |
    +--> Upload to Nexus
    |
    +--> Success
