class S1:
    CTC = 15_00_000
    bonus = (CTC * 10) / 100
    def __init__(self, id, name, skill):
        self.id = id
        self.name = name
        self.skill = skill

class S2:
    CTC = 25_00_000
    bonus = (CTC * 10) / 100
    def __init__(self, id, name, skill):
        self.id = id
        self.name = name
        self.skill = skill

class S3:
    CTC = 35_00_000
    bonus = (CTC * 10) / 100
    def __init__(self, id, name, skill):
        self.id = id
        self.name = name
        self.skill = skill

# create a function that will calculate the CTC + Bonus for each employees
# and also payroll for Ernst & Young

def calculate_payroll(list_of_employees: list):
    total = 0
    for employee in list_of_employees:
        salary = employee.CTC + employee.bonus
        print(f'{employee.name}: {salary}')
        total += salary
    print(f'Payroll by EY GDS: {total}')

aniket = S3('IN010148166', 'Aniket', ['Databricks', 'Python', 'SQL', 'Java', 'PySpark'])
pariksheet = S2('IN010148168', 'Pariksheet', ['Databricks', 'SQL'])

employee = [pariksheet, aniket]

calculate_payroll(employee)