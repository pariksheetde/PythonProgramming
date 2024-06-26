class S1:
    CTC = 15_00_000
    bonus = (CTC * 10) / 100

    def __init__(self, id, name, skill, rating=3):
        self.id = id
        self.name = name
        self.skill = skill
        self.rating = rating

class S2:
    CTC = 25_00_000
    bonus = (CTC * 10) / 100

    def __init__(self, id, name, skill, rating=3):
        self.id = id
        self.name = name
        self.skill = skill
        self.rating = rating

class S3:
    CTC = 35_00_000
    bonus = (CTC * 10) / 100

    def __init__(self, id, name, skill, rating=3):
        self.id = id
        self.name = name
        self.skill = skill
        self.rating = rating

# create a function that will calculate the CTC + Bonus for each employees
# and also payroll for Ernst & Young

def calculate_payroll(list_of_employees: list):
    total = 0
    for employee in list_of_employees:
        salary = employee.CTC + employee.bonus
        print(f'{employee.name}: {salary}')
        total += salary
    print("--------------------------------------------------------")
    print(f'Payroll by EY GDS: {total}')

bithi = S1('IN010148166', 'Bithi', ['Databricks', 'SQL', 'PySpark'], 3)
pariksheet = S3('IN010148168', 'Pariksheet', ['Databricks', 'SQL', 'Azure'], 3)
aniket = S3('IN010148166', 'Aniket', ['Databricks', 'Python', 'SQL', 'Java', 'PySpark'], 3)

employee = [pariksheet, aniket, bithi]

calculate_payroll(employee)