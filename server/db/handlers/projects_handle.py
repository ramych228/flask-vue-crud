from ..entities.project import Project


class ProjectsHandler:
    @staticmethod
    def get_all_projects(session):
        return session.query(Project).all()

    @staticmethod
    def get_project(session, project_id):
        return session.query(Project).filter_by(id=project_id).first()

    @staticmethod
    def add_project(session, name, brief):
        project = Project(name, brief)
        session.add(project)
        session.commit()
        return project

    @staticmethod
    def update_project(session, project_id, name, brief):
        project = ProjectsHandler.get_project(session, project_id)
        project.Update(name, brief)
        session.commit()
        return project

    @staticmethod
    def remove_project(session, project_id):
        session.query(Project).filter_by(id=project_id).delete()
        session.commit()
        return False

    @staticmethod
    def remove_all_projects(session):
        session.query(Project).delete()
        session.commit()
        return False
