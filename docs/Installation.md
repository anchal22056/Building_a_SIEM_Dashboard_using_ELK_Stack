# Installation Guide

## Project Name

**Building a SIEM Dashboard using ELK Stack**

---

# Overview

This guide explains how to install and run the ELK Stack project.

The project uses:

- Elasticsearch
- Logstash
- Kibana
- Python
- Docker
- Docker Compose

The setup has been tested on:

- Ubuntu 22.04
- Kali Linux
- Windows 11 (Docker Desktop)
- Oracle VirtualBox
- VMware Workstation

---

# System Requirements

Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| CPU | Dual Core |
| RAM | 8 GB |
| Storage | 20 GB Free |
| Python | 3.10 or later |
| Docker | Latest Version |
| Docker Compose | Latest Version |

Recommended Requirements

| Component | Recommendation |
|-----------|----------------|
| CPU | Quad Core |
| RAM | 16 GB |
| SSD | 30 GB Free |

---

# Software Required

Install the following software before starting.

1. Python 3

Verify installation:

```bash
python --version
```

Expected output:

```
Python 3.x.x
```

---

2. Git

Verify:

```bash
git --version
```

---

3. Docker

Verify:

```bash
docker --version
```

---

4. Docker Compose

Verify:

```bash
docker compose version
```

---

# Clone the Repository

```bash
git clone https://github.com/your-username/Building_a_SIEM_Dashboard_using_ELK_Stack.git
```

Move into the project directory:

```bash
cd Building_a_SIEM_Dashboard_using_ELK_Stack
```

---

# Install Python Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

Verify:

```bash
pip list
```

You should see packages like:

- elasticsearch
- requests
- faker
- pandas
- numpy

---

# Start the ELK Stack

Run:

```bash
docker compose up -d
```

This command starts:

- Elasticsearch
- Logstash
- Kibana

Check running containers:

```bash
docker ps
```

---

# Verify Elasticsearch

Open your browser:

```
http://localhost:9200
```

Expected response:

```json
{
  "cluster_name": "docker-cluster",
  "tagline": "You Know, for Search"
}
```

---

# Verify Kibana

Open:

```
http://localhost:5601
```

Wait a few minutes if Kibana is still starting.

---

# Generate Sample Logs

Run:

```bash
python log_generator/generate_logs.py
```

The script creates sample Apache and SSH logs.

---

# Process Logs

Logstash reads the generated logs and sends them to Elasticsearch automatically.

---

# Open Kibana Dashboard

1. Go to:

```
http://localhost:5601
```

2. Open **Dashboard**

3. Import:

```
dashboards/dashboard_export.ndjson
```

---

# Import Detection Rules

Import the following JSON files:

- brute_force.json
- failed_login.json
- port_scan.json

Location:

```
detection_rules/
```

---

# Verify the Project

Ensure:

- Elasticsearch is running
- Logstash is processing logs
- Kibana dashboards load correctly
- Security events are visible

---

# Stop the Project

```bash
docker compose down
```

---

# Common Issues

### Docker not running

Start Docker Desktop or the Docker service.

### Port 9200 already in use

Stop the conflicting process or change the port.

### Port 5601 already in use

Stop the existing Kibana instance.

### Python package not found

Run:

```bash
pip install -r requirements.txt
```

again.

---

# Next Step

Proceed to:

**Architecture.md**

to understand how data flows through the SIEM system.
