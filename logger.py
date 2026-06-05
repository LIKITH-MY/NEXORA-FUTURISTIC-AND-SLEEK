# log_interaction() function
import json
import datetime
import os

AUDIT_FILE = "audit_log.json"

if not os.path.exists(AUDIT_FILE):
    with open(AUDIT_FILE, "w") as f:
        json.dump([], f)

def log_interaction(action, query, response):
    try:
        with open(AUDIT_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "query": query,
        "response": str(response)[:500]
    })

    with open(AUDIT_FILE, "w") as f:
        json.dump(data, f, indent=2)
