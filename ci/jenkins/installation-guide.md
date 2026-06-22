# Jenkins Installation Guide

1. Install Java (JDK 17 or 21 is recommended).
2. Add Jenkins repository key and source list to your package manager.
3. Install Jenkins (`sudo apt-get install jenkins`).
4. Start Jenkins service (`sudo systemctl start jenkins`).
5. Retrieve initial admin password from `/var/lib/jenkins/secrets/initialAdminPassword`.
6. Complete web setup wizard and install suggested plugins.
