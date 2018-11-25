import threading
from websocket_server import WebsocketServer

from src.Utils.MessageHandler import MessageHandler

from src.Match import Match


class Server:
    PORT = 8090

    def __init__(self):
        self.clients = set()
        self.server = None
        self.match = None

    def start(self):
        ws_thread = threading.Thread(target=self.run)
        ws_thread.daemon = True
        ws_thread.start()

    def handle(self, match: Match):
        self.match = match

    def run(self):
        self.server = WebsocketServer(Server.PORT, host='0.0.0.0')
        self.server.set_fn_new_client(self._add_client)
        self.server.set_fn_client_left(self._client_left)
        self.server.set_fn_message_received(self._message_received)
        self.server.run_forever()

    def send(self, message):
        self.server.send_message_to_all(message)

    def send_objects(self, objects):
        if not objects:
            return

        message = MessageHandler.to_json(objects)
        self.send(message)

    def _add_client(self, client, server):
        self.clients.add(client['id'])

    def _client_left(self, client, server):
        self.clients.remove(client['id'])

    def _message_received(self, client, server, message):
        x, y, command = MessageHandler.parse(message)
        self.match.handle(command, x, y)
