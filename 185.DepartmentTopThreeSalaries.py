import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, department, left_on='departmentId', right_on='id')
    merged = merged[['name_x', 'salary', 'name_y']]
    merged.columns = ['Employee', 'Salary', 'Department']
    def top3(df):
        top_salaries = sorted(df['Salary'].unique(), reverse=True)[:3]
        return df[df['Salary'].isin(top_salaries)]
    result = merged.groupby('Department', group_keys=False).apply(top3)
    print(result)
    return result[['Department','Employee','Salary']]


data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
top_three_salaries(employee, department)