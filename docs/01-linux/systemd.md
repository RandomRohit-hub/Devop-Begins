# ⚙️ Systemd Service Management for DevOps

Systemd is the standard init system and service manager for modern Linux distributions. It is responsible for initializing user-space components and managing background daemons throughout their lifecycle.

---

## 🛠️ 1. Essential `systemctl` Commands

```bash
# Check running status, PID, memory usage, and recent log snippets
sudo systemctl status jenkins
sudo systemctl status nexus
sudo systemctl status sonarqube

# Start, stop, and restart services
sudo systemctl start jenkins
sudo systemctl stop jenkins
sudo systemctl restart jenkins

# Enable service to start automatically upon server reboot
sudo systemctl enable jenkins
sudo systemctl enable nexus
sudo systemctl enable sonarqube

# Reload systemd manager configuration after editing unit files
sudo systemctl daemon-reload
```

---

## 📄 2. Production Unit File: Sonatype Nexus

File location: `/etc/systemd/system/nexus.service`

```ini
[Unit]
Description=Sonatype Nexus Service
After=network.target

[Service]
Type=forking
LimitNOFILE=65536
ExecStart=/opt/nexus/nexus-3.78.0-14/bin/nexus start
ExecStop=/opt/nexus/nexus-3.78.0-14/bin/nexus stop
User=nexus
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

### Key Directives Explained:
* `After=network.target`: Ensures network interfaces are fully active before Nexus attempts to bind to port 8081.
* `Type=forking`: Nexus launches a background daemon process and forks from the parent caller.
* `LimitNOFILE=65536`: Increases file descriptor limits (preventing "Too many open files" when serving packages).
* `User=nexus`: Drops root privileges and runs the JVM under the unprivileged `nexus` user.
* `Restart=on-abort`: Automatically revives Nexus if it crashes abnormally.

---

## 📄 3. Production Unit File: SonarQube

File location: `/etc/systemd/system/sonarqube.service`

```ini
[Unit]
Description=SonarQube Quality Analysis Service
After=syslog.target network.target

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

### Key Directives Explained:
* `LimitNPROC=4096`: SonarQube spawns multiple child worker threads for Elasticsearch, Compute Engine, and Web Service.
* `Restart=always`: Guarantees high availability if any sub-process encounters memory exhaustion.

---

## 📜 4. Service Log Inspection with `journalctl`

Systemd routes all service `stdout` and `stderr` streams into the system journal:

```bash
# Follow logs in real time (equivalent to tail -f)
sudo journalctl -u jenkins -f
sudo journalctl -u sonarqube -f

# View logs generated during the current boot cycle only
sudo journalctl -u nexus -b

# View only the last 100 log lines
sudo journalctl -u jenkins -n 100 --no-pager

# Filter logs by priority (e.g. errors and warnings)
sudo journalctl -u jenkins -p err
```
