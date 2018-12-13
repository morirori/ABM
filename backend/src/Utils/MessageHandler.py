import json


class MessageHandler:
    @staticmethod
    def parse(message):
        data = json.loads(message)
        return data["x"], data["y"], data["command"]

    @staticmethod
    def to_json(objects: dict):
        data = {
            "team_home": [],
            "team_away": [],
            "ball": {}
        }
        for key, value in objects.items():
            if key == "ball":
                data[key] = value.to_json()
            else:
                data[key] = value.serialize()

        return json.dumps(data)
