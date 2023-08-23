from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
if __name__ == '__main__':
    calculate_salary(10)
    get_employees('Наталья Ковальская')
    print(datetime.today().date())