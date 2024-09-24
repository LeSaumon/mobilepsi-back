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

# def get_all_users(session: Session) -> List[User] | None:
#     query = select(User)
#     users = session.exec(query)
#     return users.fetchall()


# def get_user_by_member_id(member_id: int, session: Session) -> User | None:
#     query = select(User).where(User.member_id == str(member_id))
#     user = session.exec(query)
#     return user.one_or_none()


# def user_table_is_empty(session: Session) -> bool:
#     query = select(func.count()).select_from(User)
#     result = session.exec(query)
#     return True if result.first() == 0 else False


# def get_all_users_member_ids(session) -> List[str] | None:
#     query = select(User.member_id)
#     users = session.exec(query)
#     return users.fetchall()
