from data.engine import Parking
from sqlmodel import Session, select


def add_parking(parking: Parking, session: Session) -> Parking:
    session.add(parking)
    session.commit()
    session.refresh(parking)
    return parking