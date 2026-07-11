from sqlalchemy import BigInteger,String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs,DeclarativeBase):
  pass

class User(Base):
  __tablename__ = 'users'

  id : Mapped[int] = mapped_column(primary_key=True)
  tg_id : Mapped[int] = mapped_column(BigInteger, unique=True)
  tg_name : Mapped[str] = mapped_column(String(50))

  first_name : Mapped[str] = mapped_column(String(50))
  username : Mapped[str] = mapped_column(String(50), nullable=True)
  

class Category(Base):
  __tablename__ = 'categories'

  id : Mapped[int] = mapped_column(primary_key=True)
  name : Mapped[str] = mapped_column(String(20))


class Item(Base):
  __tablename__ = 'items'

  id : Mapped[int] = mapped_column(primary_key=True)
  name : Mapped[str] = mapped_column(String(20))
  description : Mapped[str] = mapped_column(String(120))
  price : Mapped[int] = mapped_column()
  category : Mapped[int] = mapped_column(ForeignKey('categories.id'))

async def async_main():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

