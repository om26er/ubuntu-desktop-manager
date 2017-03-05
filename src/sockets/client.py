import asyncio
import logging

from autobahn.asyncio.websocket import (
    WebSocketClientFactory,
    WebSocketClientProtocol,
)

LOGGER = logging.getLogger(__name__)


def get_device_id():
    with open('/etc/machine-id', 'r') as file:
        return file.read().strip()


class DesktopManagerClientProtocol(WebSocketClientProtocol):
    def onOpen(self):
        self.sendMessage(b'This is a test')

    def onClose(self, wasClean, code, reason):
        print(code, reason)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    factory = WebSocketClientFactory(
        headers={'user_identifier': 'om26er@gmail.com', 'device_id': get_device_id()})
    factory.protocol = DesktopManagerClientProtocol
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, '127.0.0.1', 9000)
    loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
