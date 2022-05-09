import contextlib
import postgres
"""
def my_context():
    # (Optional) Add any set up code you need
    yield
    # (Optional) Add any terdown code you need
"""

"""
@contextlib.contextmanager
def my_context():
    print('Hello')
    yield 42
    print('goodbye')

with my_context() as foo:
    print('foo is {}'.format(foo))
"""

@contextlib.contextmanager
def database(url):
    # set up database connection
    db = postgres.connect(url)
    
    yield db

    # tear down database connection
    db.disconnect() 

url = 'http://datacamp.com/data'
with database(url) as my_db:
    course_list = my_db.execute('SELECT * FROM courses')