import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

FILE = "jobs.json"

def load_jobs():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

class JobHandler(SimpleHTTPRequestHandler):
    pass

server = HTTPServer(("localhost", 8000), JobHandler)

print("JobTrack server running at http://localhost:8000")
server.serve_forever()
