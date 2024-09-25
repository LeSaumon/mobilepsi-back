from sqlalchemy import func
from data.engine import Pony
from sqlmodel import Session, select
from typing import List


def add_pony(pony: Pony, session: Session) -> Pony:
    session.add(pony)
    session.commit()
    session.refresh(pony)
    return pony

def get_all_pony(session: Session) -> List[Pony] | None:
    query = select(Pony)
    ponys = session.exec(query)
    return ponys.fetchall()

def get_pony_by_id(session: Session, pony_id: int) -> Pony | None:
    query = select(Pony).where(Pony.id == pony_id)
    pony = session.exec(query)
    print(pony)
    return pony.one_or_none()


def pony_table_is_empty(session: Session) -> bool:
    query = select(func.count()).select_from(Pony)
    result = session.exec(query)
    return True if result.first() == 0 else False


# def get_all_users_member_ids(session) -> List[str] | None:
#     query = select(User.member_id)
#     users = session.exec(query)
#     return users.fetchall()
