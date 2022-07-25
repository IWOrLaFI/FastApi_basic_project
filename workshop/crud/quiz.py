from workshop.crud.base import CRUDBase
from workshop.database.models.quiz import Quiz
from workshop.schemas.quiz import Quiz as QuizModel


class CRUDQuiz(CRUDBase[Quiz, QuizModel]):
    pass
