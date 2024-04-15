import csv
# with open("c:/Users/kunal/OneDrive/CODE FOR LIFE/Python projects/Python Libraries/working_with_csv_data_Pandas/popu.csv") as data_file:
    # data = data_file.readlines()
    # print(data)
    # data=csv.reader(data_file)
    # for row in data:
    #     print(row)
    # data=csv.reader(data_file)
    # population=[]
    # for row in data:
    #     population.append(row[2])
        
    # print(population)   

import pandas as pd
pd.options.display.max_rows=500
dat=pd.read_csv("c:/Users/kunal/OneDrive/CODE FOR LIFE/Python projects/Python Libraries/working_with_csv_data_Pandas/popu.csv")
# print(dat["pop"])
print(dat["pop"].mean())
print(type(dat))
print(len(dat))
print(dat.shape)
pd.set_option("display.max_rows",None)
pd.set_option("display.float_format",str)
print(dat.head(1000))
print(dat.tail(10))
print(dat.info())
basic_info=dat.info()
print(basic_info)
base=dat.describe()
print(base)
base=dat.describe(include="all")
print(base)
print(dat["pop"].describe())
print(dat["pop"].mean())
popu=pd.Series([1000,3000,500])
print(popu)
print(popu.index)#implicit index
popu=pd.Series([1000,3000,500],index=["berlin","Ukrain","London"])
print(popu)
print(popu.index)
print(popu.keys())
revenue=pd.Series({"London":1000,"Ukrain":3000,"berlin":500})
print(revenue)