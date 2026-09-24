# 🛠️ Sonatype Nexus Installation on Amazon Linux

A complete installation and service configuration guide for Sonatype Nexus 3 on Amazon Linux 2023 with Amazon Corretto 17.

---

## 🚀 1. Step-by-Step Installation Walkthrough

### Step 1: Install Amazon Corretto 17 (Java)
```bash
sudo rpm --import https://yum.corretto.aws/corretto.key
sudo curl -L -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo
sudo yum install -y java-17-amazon-corretto-devel wget tar -y

# Verify Java runtime
java -version
```

### Step 2: Download & Extract Nexus OSS
```bash
sudo mkdir -p /opt/nexus/
sudo mkdir -p /tmp/nexus/
cd /tmp/nexus/

NEXUSURL="https://download.sonatype.com/nexus/3/nexus-unix-x86-64-3.78.0-14.tar.gz"
wget $NEXUSURL -O nexus.tar.gz

# Extract archive
EXTOUT=$(tar -xzvf nexus.tar.gz)
NEXUSDIR=$(echo $EXTOUT | cut -d '/' -f1)

# Move application files and work directory to /opt/nexus
sudo rm -rf /tmp/nexus/nexus.tar.gz
sudo cp -r /tmp/nexus/* /opt/nexus/
```

### Step 3: Create Dedicated System User
```bash
sudo useradd -r -d /opt/nexus -s /bin/false nexus
sudo chown -R nexus:nexus /opt/nexus/
```

### Step 4: Configure User in `nexus.rc`
```bash
echo 'run_as_user="nexus"' | sudo tee /opt/nexus/$NEXUSDIR/bin/nexus.rc
```

---

## ⚙️ 2. Systemd Service Unit File

Create `/etc/systemd/system/nexus.service`:

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

```bash
# Reload systemd and start service
sudo systemctl daemon-reload
sudo systemctl enable nexus
sudo systemctl start nexus

# Verify running state
sudo systemctl status nexus
sudo ss -lntp | grep 8081
```

---

## 🔑 3. Initial Administrator Password & Setup Wizard

When Nexus boots for the first time, it generates a unique random password:

```bash
cat /opt/nexus/sonatype-work/nexus3/admin.password
```

1. Open your browser: `http://<NEXUS_PUBLIC_IP>:8081`.
2. Click **Sign in** in the top right.
3. **Username:** `admin`
4. **Password:** Paste the token retrieved from `admin.password`.
5. Enter a new, secure password.
6. **Configure Anonymous Access:**
   * Select **Disable anonymous access** for enterprise private repositories.
   * Anonymous access allows anyone on your network to view and download proprietary software without authentication.
