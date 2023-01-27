import pytest

from api.domain.exceptions import UserAlreadyExist
from api.domain.models import User
from api.repository.user import FakeUserRepository


from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.ext.asyncio import create_async_engine

meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))
pytestmark = pytest.mark.anyio


async def test_add_clear():
    user = User("1")
    rep = FakeUserRepository()

    res = await rep.add(user=user)

    assert res == user


async def test_add_already_exist():
    user = User("1")
    rep = FakeUserRepository()
    rep._data.append(user)

    with pytest.raises(UserAlreadyExist):
        await rep.add(user=user)


async def test_add2():
    engine = create_async_engine(
        "sqlite+aiosqlite:///db.db",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)
        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )
