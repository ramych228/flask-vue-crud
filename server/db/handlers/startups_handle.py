from ..entities.startups import Startup


class StartupsHandler:
    @staticmethod
    def get_all_startups(session):
        return session.query(Startup).all()

    @staticmethod
    def get_startup(session, startup_id):
        return session.query(Startup).filter_by(id=startup_id).first()

    @staticmethod
    def add_startup(session, name, brief):
        startup = Startup(name, brief)
        session.add(startup)
        session.commit()
        return startup

    @staticmethod
    def update_startup(session, startup_id, name, brief):
        startup = StartupsHandler.get_startup(session, startup_id)
        startup.Update(name, brief)
        session.commit()
        return startup

    @staticmethod
    def remove_startup(session, startup_id):
        session.query(Startup).filter_by(id=startup_id).delete()
        session.commit()
        return False

    @staticmethod
    def remove_all_startups(session):
        session.query(Startup).delete()
        session.commit()
        return False

