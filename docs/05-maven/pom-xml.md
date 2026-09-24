# 📄 Maven POM.xml Deep-Dive & Coordinates

The `pom.xml` (Project Object Model) file is the core configuration unit in a Maven project. It provides all information Maven needs to build the software.

---

## 🧭 1. Maven Coordinates (GAV)

Every Maven artifact in the world is uniquely addressed by three coordinates: **GAV** (**G**roupId, **A**rtifactId, **V**ersion):

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <!-- 1. Group Identifier (Usually company reverse-DNS) -->
  <groupId>com.visualpathit</groupId>

  <!-- 2. Artifact Identifier (Project name) -->
  <artifactId>vprofile-project</artifactId>

  <!-- 3. Version of the deliverable -->
  <version>v2</version>

  <!-- 4. Packaging type (jar, war, pom) -->
  <packaging>war</packaging>
</project>
```

* **`groupId`:** Defines the organization or namespace (e.g. `org.springframework`, `com.visualpathit`).
* **`artifactId`:** The base name of the generated file (e.g. `vprofile-project`).
* **`version`:** The current development or release version (e.g. `v2`, `1.0.0-SNAPSHOT`).
* **`packaging`:** The resulting binary format. For web applications running on Tomcat, packaging is `<packaging>war</packaging>`.

---

## 📦 2. Managing Dependencies

Instead of manually checking third-party JARs into Git:

```xml
<dependencies>
  <!-- Spring Web MVC -->
  <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.3.30</version>
  </dependency>

  <!-- MySQL JDBC Driver -->
  <dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
  </dependency>

  <!-- JUnit for Testing (Scoped only to test phase) -->
  <dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
  </dependency>
</dependencies>
```

### Dependency Scopes:
* `compile` (Default): Needed during compile, test, and runtime packaging.
* `provided`: Needed during compile and test, but expected to be provided by the runtime servlet container (e.g. Tomcat provides `servlet-api`).
* `test`: Needed only during test compilation and execution (e.g. `junit`, `mockito`); omitted from the final WAR package.
* `runtime`: Not needed for compilation, but required during execution (e.g. JDBC database drivers).
