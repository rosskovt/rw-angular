from .entities.entity import engine, Base, Session
from .entities.exam import Exam, ExamSchema
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

Base.metadata.create_all(engine)


@app.route('/exams')
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()

    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)
    session.close()
    return jsonify(exams.data)


@app.route('/add_exam', methods=['POST'])
def add_exam():
    posted_exam = ExamSchema(only=('title', 'description')) \
        .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201


# if __name__ == '__main__':
