# Building a SIEM Dashboard using ELK Stack

## Project Overview

This project demonstrates how to build a Security Information and Event Management (SIEM) dashboard using the ELK Stack (Elasticsearch, Logstash, and Kibana).

The dashboard collects logs generated from simulated Apache web servers and SSH authentication logs, processes them through Logstash, stores them in Elasticsearch, and visualizes security events in Kibana.

The project also includes custom detection rules for identifying:

- Brute Force Attacks
- Failed Login Attempts
- Port Scanning Activities

---

# Objectives

- Learn ELK Stack architecture
- Collect and parse logs
- Store logs in Elasticsearch
- Visualize events in Kibana
- Detect suspicious activities
- Build a cybersecurity monitoring dashboard

---

# Technologies Used

- Python 3
- Elasticsearch
- Logstash
- Kibana
- Docker
- Docker Compose
- Git
- Linux

---

# Project Structure

```
Building_a_SIEM_Dashboard_using_ELK_Stack/
│
├── README.md
├── LICENSE
├── requirements.txt
├── docker-compose.yml
├── .gitignore
│
├── docs/
│   ├── Installation.md
│   ├── Architecture.md
│   ├── Dashboard.md
│   ├── Detection_Rules.md
│   └── Troubleshooting.md
│
├── log_generator/
│   ├── generate_logs.py
│   ├── apache_logs.py
│   └── ssh_logs.py
│
├── logstash/
│   └── logstash.conf
│
├── elasticsearch/
│   └── elasticsearch.yml
│
├── kibana/
│   └── kibana.yml
│
├── dashboards/
│   └── dashboard_export.ndjson
│
├── detection_rules/
│   ├── brute_force.json
│   ├── failed_login.json
│   └── port_scan.json
│
├── reports/
│   └── Final_Report.pdf
│
└── screenshots/
    ├── dashboard.png
    ├── kibana.png
    └── elasticsearch.png
```

---

# Features

- Simulated security log generation
- Real-time log ingestion
- Dashboard visualization
- Detection of attacks
- Custom Logstash pipeline
- Docker-based deployment

---

# Workflow

```
Python Log Generator
        |
        |
        V
    Log Files
        |
        |
        V
    Logstash
        |
        |
        V
 Elasticsearch
        |
        |
        V
     Kibana Dashboard
```

---

# Installation

Follow the guide in:

docs/Installation.md

---

# Dashboard

The dashboard displays:

- Failed Login Attempts
- SSH Authentication Logs
- Apache Requests
- Top Source IP Addresses
- HTTP Status Codes
- Brute Force Attempts
- Port Scan Detection

---

# Detection Rules

Included detection rules:

- Brute Force
- Failed Login
- Port Scan

---

# Screenshots

After running the project, upload screenshots inside

```
screenshots/
```

---

# Future Improvements

- Email Alerting
- Slack Notifications
- Threat Intelligence Integration
- GeoIP Visualization
- Machine Learning Anomaly Detection

---

# Author

Cybersecurity ELK Stack Project

