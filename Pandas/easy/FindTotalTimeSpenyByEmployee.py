import pandas as pd 
from pandas import Series , DataFrame




employees = DataFrame(
    {
        "emp_id":[1,1,1,2,2] ,
        "event_day":["2020-11-28","2020-11-28","2020-12-03","2020-11-28","2020-12-09" ],
        "in_time":[4,55,1,3,47] , 
        "out_time": [32,200,42,33,74]
    }
)

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["event_day"] = pd.to_datetime(employees["event_day"] )

    employees["total_time"] = employees["out_time"] - employees["in_time"]
    # print(employees)
    # print(employees.dtypes)



    result = employees.groupby(["event_day" , "emp_id"]).sum()
    result = result.drop(["in_time","out_time"] , axis=1).unstack()
    print(result)
    # return result.sort_values(by="emp_id")
    

table = total_time(employees=employees)
print(table)
print(table.dtypes)