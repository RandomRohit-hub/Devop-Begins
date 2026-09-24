# 🛠️ SonarQube Enterprise Installation & Host Tuning

A complete production installation guide for SonarQube on Ubuntu 24.04 LTS with a dedicated PostgreSQL database and Linux kernel performance tuning.

---

## ⚙️ 1. Mandatory Linux Kernel Tuning

SonarQube's embedded Elasticsearch search engine strictly requires specific kernel parameters. Without these settings, Elasticsearch will abort on boot.

### Step 1: Virtual Memory & File Handles (`/etc/sysctl.conf`)
```bash
sudo cp /etc/sysctl.conf /etc/sysctl.conf.bak
sudo tee -a /etc/sysctl.conf <<EOT
vm.max_map_count=262144
fs.file-max=65536
EOT

# Apply immediately without reboot
sudo sysctl -p
```

### Step 2: User Process & File Descriptors (`/etc/security/limits.conf`)
```bash
sudo cp /etc/security/limits.conf /etc/security/limits.conf.bak
sudo tee -a /etc/security/limits.conf <<EOT
sonarqube   -   nofile   65536
sonarqube   -   nproc    4096
EOT
```

---

## 🐘 2. PostgreSQL Database Provisioning

SonarQube requires an external relational database for storing project metadata, user accounts, and historical quality gates.

```bash
# Install PostgreSQL repository and packages
sudo apt update
sudo apt install postgresql postgresql-contrib -y

# Start and enable PostgreSQL service
sudo systemctl enable --now postgresql.service

# Create Sonar database user and database with encrypted credentials
sudo -i -u postgres psql -c "CREATE USER sonar WITH ENCRYPTED PASSWORD 'AdminSecretDB2026!';"
sudo -i -u postgres psql -c "CREATE DATABASE sonarqube OWNER sonar;"
sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonar;"

# Restart PostgreSQL to apply
sudo systemctl restart postgresql
```

> [!WARNING]
> Never use generic tutorial passwords like `admin123` in real cloud environments!

---

## 📦 3. SonarQube Application Installation

### Step 1: Install OpenJDK 21 or 17
```bash
sudo apt update
sudo apt install openjdk-21-jdk -y
```

### Step 2: Download & Extract SonarQube Community Edition
```bash
sudo mkdir -p /opt/sonarqube
cd /tmp
sudo wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-26.4.0.121862.zip
sudo apt install zip -y
sudo unzip -o sonarqube-26.4.0.121862.zip -d /opt/
sudo mv /opt/sonarqube-*/* /opt/sonarqube/
```

### Step 3: Create Dedicated System User & Grant Ownership
```bash
sudo groupadd sonar
sudo useradd -c "SonarQube System User" -d /opt/sonarqube/ -g sonar -s /bin/bash sonar
sudo chown -R sonar:sonar /opt/sonarqube/
```

### Step 4: Configure Database Connection (`sonar.properties`)
File: `/opt/sonarqube/conf/sonar.properties`
```ini
sonar.jdbc.username=sonar
sonar.jdbc.password=AdminSecretDB2026!
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
sonar.web.host=0.0.0.0
sonar.web.port=9000
sonar.web.javaAdditionalOpts=-server -Xmx1024m
sonar.search.javaOpts=-Xmx512m -Xms512m
sonar.log.level=INFO
sonar.path.logs=logs
```

---

## 🚀 4. Systemd Service Configuration

File: `/etc/systemd/system/sonarqube.service`
```ini
[Unit]
Description=SonarQube Service
After=syslog.target network.target postgresql.service

[Service]
Type=forking
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
User=sonar
Group=sonar
Restart=always
LimitNOFILE=65536
LimitNPROC=4096

[Install]
WantedBy=multi-user.target
```

```bash
# Reload systemd and start SonarQube
sudo systemctl daemon-reload
sudo systemctl enable sonarqube.service
sudo systemctl start sonarqube.service

# Verify service is running
sudo systemctl status sonarqube.service
sudo ss -lntp | grep 9000
```
