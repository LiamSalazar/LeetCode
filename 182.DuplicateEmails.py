import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    visited = []
    repeated = []
    for email in person['email']:
        if email in visited and email not in repeated:
            repeated.append(email)
        else:
            visited.append(email)
    result = {'Email': repeated}
    return pd.DataFrame(result)