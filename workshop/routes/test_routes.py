from fastapi import APIRouter, Depends, status
from workshop.schemas.referencing import TextModel, TextInfoResponse, TextCreateResponse
from workshop.dependencies.crud_dependency import get_text_crud_dependency
from workshop.database.session import get_db
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from workshop.utils.exceptions import TextNotFound
from workshop.crud.text import CRUDText
router = APIRouter(tags=["test"])


@router.get('/test')
def test_endpoint():
    return{'messege':'test!'}



@router.post("/referencing/add_text/", response_model=TextCreateResponse)
async def add_text(text_example: TextModel, crud: CRUDText = Depends(get_text_crud_dependency),
                   db: Session = Depends(get_db)) -> JSONResponse:
    result = await crud.create(db=db, obj_in=text_example)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"id": result.id, "text": result.your_text})
    