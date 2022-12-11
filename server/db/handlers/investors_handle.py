from ..entities.investor import Investor


class InvestorsHandler:
    @staticmethod
    def get_all_investors(session):
        return session.query(Investor).all()

    @staticmethod
    def get_investor_by_id(session, investor_id):
        return session.query(Investor).filter_by(id=investor_id).first()

    @staticmethod
    def get_investor_by_username(session, username):
        return session.query(Investor).filter_by(username=username).first()

    @staticmethod
    def add_investor(session, name, brief):
        investor = Investor(name, brief)
        session.add(investor)
        session.commit()
        return investor

    @staticmethod
    def update_investor(session, investor_id, name, brief):
        investor = InvestorsHandler.get_investor(session, investor_id)
        investor.Update(name, brief)
        session.commit()
        return investor

    @staticmethod
    def remove_investor(session, investor_id):
        session.query(Investor).filter_by(id=investor_id).delete()
        session.commit()
        return False

    @staticmethod
    def remove_all_investors(session):
        session.query(Investor).delete()
        session.commit()
        return False
