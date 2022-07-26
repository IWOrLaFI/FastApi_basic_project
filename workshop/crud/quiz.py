from sqlalchemy.orm import Session

from workshop.database.models.quiz import Quiz, Question, Answer
from workshop.database.schemas.quiz import QuizInfo, QuestionInfo, AnswerInfo


def create_quiz(db: Session, quiz: QuizInfo):
    db_quiz = Quiz(id=quiz.id,
                   title=quiz.title,
                   description=quiz.description,
                   total_questions=quiz.total_questions,
                   quiz_score=quiz.quiz_score,
                   email=quiz.owner_email)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz


def delete_quiz(db: Session, quiz_title: str):
    quiz = db.query(Quiz).filter(Quiz.title == quiz_title).first()
    db.delete(quiz)
    db.commit()
    return db.query(Quiz).all()


def get_quiz_by_title(db: Session, quiz_title: str):
    quiz = db.query(Quiz).filter(Quiz.title == quiz_title).first()
    return quiz


def get_quiz_by_id(db: Session, quiz_id: int):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    return quiz


def get_quizzes(db: Session, owner_email: str):
    return db.query(Quiz).filter(Quiz.owner_email == owner_email).all()


def update_quiz_score(db: Session, quiz_id: int, user_points: int):
    update = db.query(Quiz).filter(Quiz.id == quiz_id).update({'quiz_score': user_points})
    db.commit()
    user_points = db.query(Quiz.quiz_score).filter(Quiz.id == quiz_id).first()
    return user_points


def create_question(db: Session, question: QuestionInfo):
    db_question = Question(question=question.question, owner_id=question.owner_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_question(db: Session, question: str):
    question = db.query(Question).filter(Question.question == question).first()
    return question


def delete_question(db: Session, question: str):
    question = db.query(Question).filter(Question.question == question).first()
    db.delete(question)
    db.commit()
    return db.query(Question).all()


def get_questions_info(db: Session, quiz_id: int):
    return db.query(Question).filter(Question.owner_id == quiz_id).all()


def get_questions(db: Session, quiz_id: int):
    return db.query(Question.question).filter(Question.owner_id == quiz_id).all()


def create_answer(db: Session, answer: AnswerInfo):
    db_answer = Answer(answers=answer.answers,
                       correct_answer=answer.correct_answer,
                       owner_id=answer.owner_id)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def get_answer(db: Session, answer: str):
    answer = db.query(Answer).filter(Answer.answers == answer).first()
    return answer


def delete_answer(db: Session, answer: str):
    answer = db.query(Answer).filter(Answer.answers == answer).first()
    db.delete(answer)
    db.commit()
    return db.query(Answer).all()


def get_answers_info(db: Session, question_id: int):
    return db.query(Answer).filter(Answer.owner_id == question_id).all()


def get_answers(db: Session, question_id: int):
    return db.query(Answer.answers).filter(Answer.owner_id == question_id).all()


def get_correct_answers(db: Session, question_id: int):
    return db.query(Answer.correct_answer).filter(Answer.owner_id == question_id).all()



