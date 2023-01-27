import abc

from api.domain import exceptions, models


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, user: models.User):
        ...


class FakeUserRepository(AbstractUserRepository):
    def __init__(self) -> None:
        self._data: list[models.User] = []

    async def add(self, user: models.User):
        if user in self._data:
            raise exceptions.UserAlreadyExist
        else:
            self._data.append(user)
            return user


class SQLAlchemyRepository(AbstractUserRepository):
    def __init__(self, session) -> None:
        self.session = session

    async def add(self, user: models.User):
        return await super().add(user)
