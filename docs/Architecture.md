# SIEM Architecture

## Components

```
Python Log Generator
        │
        ▼
Logstash
        │
        ▼
Elasticsearch
        │
        ▼
Kibana Dashboard
```

---

## Data Flow

1. Python generates logs.
2. Logstash parses logs.
3. Elasticsearch stores indexed logs.
4. Kibana visualizes the data.
5. Detection rules trigger alerts.

---

## Technologies

- Python
- Elasticsearch
- Logstash
- Kibana
- Linux
- JSON
