from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db_tables import s_main, performance

engine = create_engine('postgresql://baza:baza534@localhost:5432/phones')

session = Session(bind=engine)


def short_desc(model: str):
    r = session.query(performance.c.title,
                      performance.c.storage_size).filter(performance.c.title == model).first()
    return r


print(*short_desc('Honor 80'))
