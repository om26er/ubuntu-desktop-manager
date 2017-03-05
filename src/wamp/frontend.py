import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

from src import constants


class MyComponent(ApplicationSession):
    async def onJoin(self, details):
        if not await self.call(constants.RPC_IS_SCREEN_LOCKED):
            await self.call(constants.RPC_LOCK_SCREEN)
        bytes_data = await self.call(constants.RPC_GRAB_SCREENSHOT)
        with open('output.png', 'wb') as output:
            output.write(bytes_data)
        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    runner = ApplicationRunner(
        url=u'ws://188.166.150.190:8080/ws', realm=u'realm1')
    runner.run(MyComponent)
