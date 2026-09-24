# 🔨 Apache Maven Overview & Standard Layout

Apache Maven is a software project management and comprehension tool primarily used for Java applications. Based on the concept of a Project Object Model (POM), Maven manages a project's build, reporting, and documentation from a central piece of information.

---

## 🎯 1. Why Maven? (Convention over Configuration)

Before Maven, Java projects used Apache Ant with complex, custom XML build scripts where developers had to manually define every compilation directory, classpath, and file copy step.

Maven introduced **Convention over Configuration**: if a project follows standard folder layouts, Maven can compile, test, and package the application with zero custom build scripts.

```text
my-app/
├── pom.xml                     -> Project Object Model definition
└── src/
    ├── main/
    │   ├── java/               -> Production Java source code (.java)
    │   ├── resources/          -> Configuration files (db.properties, logback.xml)
    │   └── webapp/             -> Web assets for WAR packaging (JSP, CSS, WEB-INF/web.xml)
    └── test/
        ├── java/               -> JUnit / TestNG test classes (.java)
        └── resources/          -> Test configuration files
```

When built, Maven creates the output directory:
```text
target/
├── classes/                    -> Compiled production bytecode (.class)
├── test-classes/               -> Compiled test bytecode
└── vprofile-v2.war             -> Final packaged deployable archive
```

---

## 🤝 2. The Relationship Between Jenkins and Maven

> [!IMPORTANT]
> **Key Distinction:**
> * Jenkins does **not** compile Java source code.
> * Jenkins provides the orchestrator environment (`tools { maven "MAVEN3.9" }`).
> * Jenkins invokes the Maven binary (`sh 'mvn test'`).
> * Maven reads `pom.xml`, downloads required libraries, compiles the code, executes tests, and packages the WAR.
> * Jenkins captures Maven's exit status (`0` = Success, non-zero = Failure).
