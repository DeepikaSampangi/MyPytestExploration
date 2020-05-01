import pytest
import basic_pytest_examples.math_functions as mathfun

## py.test -v gives us specifiacally the state of each test within a file PASS or FAILED
## To run a specific test within the test file command $ pytest <test_file_name>::test_name
## To run the tests within a file with a specific key word give the command $ pytest -v -k "<keyword> or/and <keyword>..."
## To run a test with specific marker $ pytest -v -m "<marker>"
## To exit at the very first failure $ pytest -v -x
## To avoid the stack trace $ pytest --tb=no
## to Allow any print statement defined within the tests $ pytest -v -s or $ pytest -v --capture=no
## for a brief info of the tests passed $ pytest -q

# @pytest.mark.numbers
def test_add_num():
    assert mathfun.add_num(2,3) == 5

# @pytest.mark.numbers
def test_sq_num():
    assert mathfun.sq_num(2) == 4

# @pytest.mark.strings
# @pytest.mark.skip('message for skipping')
def test_add_str():
    res = mathfun.add_num('Hey', 'There')
    assert res == 'HeyThere'
    assert type(res) is str
    assert 'Hey' in res
    assert 'Hello There' not in res


## using parameterize decorator within the mark inialise a string with all the var comma separated
# then following it define the input to be given in a list of tuples

@pytest.mark.parametrize('num1, num2, result', [(2,3,5), (5,4,9), ('deep','ika','deepika')])
def test_add_num_params(num1, num2, result):
    assert mathfun.add_num(num1, num2) == result