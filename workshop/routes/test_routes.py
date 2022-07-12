from fastapi import APIRouter

router = APIRouter(tags=["test"])


@router.get('/test')
def test_endpoint():
    return{'messege':'test!'}

