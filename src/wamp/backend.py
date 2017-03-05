from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

from src import display
from src import constants


class MyComponent(ApplicationSession):
    async def onJoin(self, details):
        await self.register(
            display.is_locked, constants.RPC_IS_SCREEN_LOCKED)
        await self.register(display.lock, constants.RPC_LOCK_SCREEN)
        await self.register(
            display.grab_screenshot, constants.RPC_GRAB_SCREENSHOT)


if __name__ == '__main__':
    runner = ApplicationRunner(
        url=u'ws://188.166.150.190:8080/ws', realm=u'realm1')
    runner.run(MyComponent)
