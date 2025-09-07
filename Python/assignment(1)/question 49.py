#)Write a Python script to concatenate following dictionaries to create 
#a new one

dict1={1:'apple',2:'banana'}

dict2={3:'grape',4:'cherry'}

dict3={5:'abc',6:'xyz'}

dict_new={}
for d in (dict1,dict2,dict3):
    dict_new.update(d)

print(dict_new)