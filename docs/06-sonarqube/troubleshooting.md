# 🩺 SonarQube Troubleshooting & Diagnostics

A diagnostic runbook for resolving SonarQube service crashes, database connection errors, and pipeline timeouts.

---

## 🚨 1. SonarQube Starts then Crashes Immediately (Elasticsearch Error)

### Symptoms:
Running `sudo systemctl status sonarqube` shows `Active: failed (Result: exit-code)`.
Inspecting `/opt/sonarqube/logs/es.log`:
```text
max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

### Fix:
Apply the sysctl virtual memory fix:
```bash
sudo sysctl -w vm.max_map_count=262144
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
sudo systemctl restart sonarqube
```

---

## 🚨 2. PostgreSQL Connection Failure

### Symptoms:
Inspecting `/opt/sonarqube/logs/sonar.log`:
```text
FATAL: password authentication failed for user "sonar"
Or: Connection to localhost:5432 refused.
```

### Fix:
1. Verify PostgreSQL service is active: `sudo systemctl status postgresql`.
2. Test database login manually via psql:
   ```bash
   psql -h localhost -U sonar -d sonarqube
   ```
3. Verify password inside `/opt/sonarqube/conf/sonar.properties` matches the encrypted password assigned in PostgreSQL.

---

## 🚨 3. Jenkins Pipeline Hangs at `waitForQualityGate`

### Symptoms:
The Jenkins build executes `mvn sonar:sonar` successfully, but the next stage hangs for 5 minutes and times out.

### Root Cause:
SonarQube has not sent the webhook callback to Jenkins (or the network blocked it).

### Fix Checklist:
1. Open SonarQube: **Administration ➔ Configuration ➔ Webhooks**.
2. Verify the Webhook URL is set to `http://<JENKINS_IP>:8080/sonarqube-webhook/` (trailing slash is mandatory!).
3. Verify Jenkins Security Group allows inbound TCP 8080 from the SonarQube server's Security Group (`Sonar-SG`).
4. Click the gear icon next to the webhook in SonarQube and check **Recent Deliveries** for HTTP 200 vs HTTP 403/Timeout.
