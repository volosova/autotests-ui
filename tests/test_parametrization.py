import pytest  
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number,expected", [(1,1), (2, 4), (3,9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len (os + browser) > 0

@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request: SubRequest) -> str:
    return request.param 

def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")