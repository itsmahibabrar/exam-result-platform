# exam-result-platform

A basic modular Flask + SQLite starter for an exam result platform.

## Project structure

```text
app/
  config.py
  db.py
  schema.sql
  modules/
    results/
      routes.py
tests/
run.py
requirements.txt
```

## Run locally

```bash
python -m pip install -r requirements.txt
python run.py
```

## Quick check

```bash
python -m unittest discover -s tests
```
