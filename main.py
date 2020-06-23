from application.people import get_employees
from application.salary import get_salary
from datetime import datetime
from dirty_main import *

if __name__ == '__main__':
    print(datetime.now())
    get_employees()