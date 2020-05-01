import pytest
from basic_pytest_examples.student_db import StudentDB

def test_alex_data():
    db = StudentDB()
    db.connector('basic_pytest_examples/tests/student_data.json')
    alex_data = db.get_data('Alex')
    assert alex_data['id'] == 1
    assert alex_data['name'] == 'Alex'
    assert alex_data['result'] == 'Pass'

def test_jack_data():
    db = StudentDB()
    db.connector('basic_pytest_examples/tests/student_data.json')
    jack_data = db.get_data('Jack')
    assert jack_data['id'] == 2
    assert jack_data['name'] == 'Jack'
    assert jack_data['result'] == 'Fail'


## But in order to avoid repition of code and calls a method everytime, it can be handled by using either setup_module or teardown module

##setup_module, will be called at the start of the pytest

glb_db = None

def setup_module(module):
    global glb_db
    glb_db = StudentDB()
    glb_db.connector('basic_pytest_examples/tests/student_data.json')

def test_alex_data_glb():
    alex_data = glb_db.get_data('Alex')
    assert alex_data['id'] == 1
    assert alex_data['name'] == 'Alex'
    assert alex_data['result'] == 'Pass'

def test_jack_data_glb():
    jack_data = glb_db.get_data('Jack')
    assert jack_data['id'] == 2
    assert jack_data['name'] == 'Jack'
    assert jack_data['result'] == 'Fail'


## teardown_module, used to close the connections made, after pytest is done, then teradown is run

def teardown_module(module):
    glb_db.close()



## using pytest fixtures
## setup of db fixture would be called as many tests use the setup, but to limit it set the scope to module for the fixtures
## you can also add a close connection after evrything is done by giving yield instead of return and define next steps

@pytest.fixture(scope='module')
def pyfix_db():
    pyfix_db =StudentDB()
    pyfix_db.connector('basic_pytest_examples/tests/student_data.json')
    return pyfix_db
    # yeild pyfix_db
    # pyfix_db.close()

def test_alex_data_pyfix(pyfix_db):
    alex_data = pyfix_db.get_data('Alex')
    assert alex_data['id'] == 1
    assert alex_data['name'] == 'Alex'
    assert alex_data['result'] == 'Pass'

def test_jack_data_pyfix(pyfix_db):
    jack_data = pyfix_db.get_data('Jack')
    assert jack_data['id'] == 2
    assert jack_data['name'] == 'Jack'
    assert jack_data['result'] == 'Fail'