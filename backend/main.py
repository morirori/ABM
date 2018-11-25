import time
from src.WebSockets.Server import Server
from src.Match.Match import Match

if __name__ == "__main__":
    match = Match()
    ws_server = Server()
    ws_server.start()
    ws_server.handle(match)
    while True:
        if match.running:
            match.process()
            ws_server.send_objects(match.objects)
        # 60 fps
        time.sleep(1/60)
