# Troubleshooting

## Elasticsearch not starting

Check

```bash
sudo systemctl status elasticsearch
```

---

## Kibana not loading

Restart

```bash
sudo systemctl restart kibana
```

---

## Logstash pipeline errors

```bash
sudo journalctl -u logstash
```

---

## Logs not appearing

Check

```bash
curl localhost:9200/_cat/indices?v
```

---

## Python script not generating logs

Verify Python

```bash
python3 --version
```

Install packages

```bash
pip install faker
```
