import json

class Storage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
