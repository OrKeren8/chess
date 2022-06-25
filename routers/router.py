from fastapi import APIRouter
from . import deps

func = deps.get_func()

router = APIRouter(
    prefix="/service_name",
    tags=["service name"]
)

@router.get('/')
def hello_page():
    return 'hello'

@router.post('/do-something')
def do_something():
    return func.do_something()
