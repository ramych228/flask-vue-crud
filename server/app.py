from flask import Flask, jsonify, request
from flask_cors import CORS
from db.dbsetup import DBSetup
from db.handlers.students_handle import StudentsHandler
from db.handlers.projects_handle import ProjectsHandler

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

db = DBSetup('db.db')
db.reset_db()
session = db.get_session()

StudentsHandler.add_student(session, 'John', 'A student')
StudentsHandler.add_student(session, 'Jane', 'A student')
StudentsHandler.add_student(session, 'Johnsdsd', 'A student')

ProjectsHandler.add_project(session, 'Project 1', 'A project')
ProjectsHandler.add_project(session, 'Project 2', 'A project')
ProjectsHandler.add_project(session, 'Project 3', 'A project')


# sanity check route
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/api/students', methods=['GET'])
def get_all_students():
    response_object = {'status': 'success'}
    students = StudentsHandler.get_all_students(session)
    response_object['message'] = 'Students retrieved successfully'
    response_object['students'] = [student.serialize() for student in students]
    return jsonify(response_object)


@app.route('/api/students/<student_id>', methods=['GET'])
def get_student(student_id):
    response_object = {'status': 'success'}
    student = StudentsHandler.get_student(session, student_id)
    response_object['message'] = 'Student retrieved successfully'
    response_object['student'] = student.serialize()
    return jsonify(response_object)


@app.route('/api/students', methods=['POST'])
def add_student():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    student = StudentsHandler.add_student(session, post_data.get('name'), post_data.get('brief'))
    response_object['message'] = 'Student added successfully'
    response_object['student'] = student.serialize()
    return jsonify(response_object)


@app.route('/api/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    student = StudentsHandler.update_student(session, student_id, post_data.get('name'), post_data.get('brief'))
    response_object['message'] = 'Student updated successfully'
    response_object['student'] = student.serialize()
    return jsonify(response_object)


@app.route('/api/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    response_object = {'status': 'success'}
    status = StudentsHandler.remove_student(session, student_id)
    if status:
        response_object['message'] = 'Student removed successfully'
    else:
        response_object['message'] = 'Student not removed'
    return jsonify(response_object)


@app.route('/api/students', methods=['DELETE'])
def delete_all_students():
    response_object = {'status': 'success'}
    status = StudentsHandler.remove_all_students(session)
    if status:
        response_object['message'] = 'All students removed successfully'
    else:
        response_object['message'] = 'All students not removed'
    return jsonify(response_object)


@app.route('/api/projects', methods=['GET'])
def get_all_projects():
    response_object = {'status': 'success'}
    projects = ProjectsHandler.get_all_projects(session)
    response_object['message'] = 'Projects retrieved successfully'
    response_object['projects'] = [project.serialize() for project in projects]
    return jsonify(response_object)


@app.route('/api/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    response_object = {'status': 'success'}
    project = ProjectsHandler.get_project(session, project_id)
    response_object['message'] = 'Project retrieved successfully'
    response_object['project'] = project.serialize()
    return jsonify(response_object)


@app.route('/api/projects', methods=['POST'])
def add_project():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    project = ProjectsHandler.add_project(session, post_data.get('name'), post_data.get('brief'))
    response_object['message'] = 'Project added successfully'
    response_object['project'] = project.serialize()
    return jsonify(response_object)


@app.route('/api/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    project = ProjectsHandler.update_project(session, project_id, post_data.get('name'), post_data.get('brief'))
    response_object['message'] = 'Project updated successfully'
    response_object['project'] = project.serialize()
    return jsonify(response_object)


@app.route('/api/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    response_object = {'status': 'success'}
    status = ProjectsHandler.remove_project(session, project_id)
    if status:
        response_object['message'] = 'Project removed successfully'
    else:
        response_object['message'] = 'Project not removed'
    return jsonify(response_object)


@app.route('/api/projects', methods=['DELETE'])
def delete_all_projects():
    response_object = {'status': 'success'}
    status = ProjectsHandler.remove_all_projects(session)
    if status:
        response_object['message'] = 'All projects removed successfully'
    else:
        response_object['message'] = 'All projects not removed'
    return jsonify(response_object)






if __name__ == '__main__':
    app.run()
