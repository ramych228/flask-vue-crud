from ..entities.student import Student


class StudentsHandler:
    @staticmethod
    def get_all_students(session):
        return session.query(Student).all()

    @staticmethod
    def get_student(session, student_id):
        return session.query(Student).filter_by(id=student_id).first()

    @staticmethod
    def add_student(session, name, description):
        student = Student(name, description)
        session.add(student)
        session.commit()
        return student

    @staticmethod
    def update_student(session, student_id, name, description):
        student = StudentsHandler.get_student(session, student_id)
        student.update(name, description)
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
