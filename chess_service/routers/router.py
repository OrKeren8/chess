from fastapi import APIRouter
from . import deps

webdriver = deps.get_webdriver()

router = APIRouter(
    prefix="/web-driver",
    tags=["web driver"]
)

@router.get('/')
def hello_page():
    return 'hello'

@router.post('/open-game')
def open_game():
    return webdriver.open_page()
