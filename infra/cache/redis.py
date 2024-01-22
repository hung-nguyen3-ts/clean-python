from typing import Any

from redis.asyncio import Redis


class CustomRedisClient(Redis):
    # call_assignment_blocking_channel: str
    # call_assignment_blocking_pubsub: PubSub
    _lock_timeout: float
    _lock_blocking_timeout: float

    @staticmethod
    def get_redis_client(
        host: str,
        port: int,
        db: int,
        password: str,
        lock_timeout: float,
        lock_blocking_timeout: float,
    ) -> "CustomRedisClient":
        redis_client = CustomRedisClient(
            host=host,
            port=port,
            db=db,
            password=password,
            decode_responses=True,
        )
        redis_client._lock_timeout = lock_timeout
        redis_client._lock_blocking_timeout = lock_blocking_timeout
        return redis_client

    # async def setup_call_assignment_blocking_pubsub(
    #     self,
    #     call_assignment_blocking_channel: str,
    # ):
    #     self.call_assignment_blocking_channel = call_assignment_blocking_channel
    #     self.call_assignment_blocking_pubsub = self.pubsub(
    #         ignore_subscribe_messages=True
    #     )
    #     await self.call_assignment_blocking_pubsub.subscribe(
    #         self.call_assignment_blocking_channel
    #     )

    def lock(
        self,
        name: str,
        timeout: float | None = None,
        sleep: float = 0.1,
        blocking: bool = True,
        blocking_timeout: float | None = None,
        lock_class: Any | None = None,
        thread_local: bool = True,
    ):
        if timeout is None:
            timeout = self._lock_timeout
        if blocking_timeout is None:
            blocking_timeout = self._lock_blocking_timeout

        return super().lock(
            name, timeout, sleep, blocking, blocking_timeout, lock_class, thread_local
        )
