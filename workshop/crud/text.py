from workshop.crud.base import CRUDBase
from workshop.database.models.text import Text
from workshop.schemas.referencing import TextModel


class CRUDText(CRUDBase[Text, TextModel]):
    pass