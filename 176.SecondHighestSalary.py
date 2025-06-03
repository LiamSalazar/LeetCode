import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee['salary'].unique().sort()
    salary.sort()
    return pd.DataFrame({'SecondHighestSalary': [salary[-2]]}) if len(salary) > 0 else pd.DataFrame({'SecondHighestSalary': [None]})


data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
second_highest_salary(employee)