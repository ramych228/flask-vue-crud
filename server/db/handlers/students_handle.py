from ..entities.student import Student


class StudentsHandler:
    @staticmethod
    def get_all_students(session):
        return session.query(Student).all()

    @staticmethod
    def get_student_by_id(session, student_id):
        return session.query(Student).filter_by(id=student_id).first()

    @staticmethod
    def get_student_by_username(session, username):
        return session.query(Student).filter_by(username=username).first()

    @staticmethod
    def add_student(session, name, description, username, password, token):
        student = Student(name, description, username, password, token)
        session.add(student)
        session.commit()
        return student

    @staticmethod
    def update_student(session, student_id, name, description, username, password, token):
        student = StudentsHandler.get_student_by_id(session, student_id)
        student.Update(name, description, username, password, token)
        session.commit()
        return student

    @staticmethod
    def remove_student(session, student_id):
        session.query(Student).filter_by(id=student_id).delete()
        session.commit()
        return False

    @staticmethod
    def remove_all_students(session):
        session.query(Student).delete()
        session.commit()
        return False
