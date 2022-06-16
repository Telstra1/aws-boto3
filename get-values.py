import json

user_obj = input("Enter the object:")
user_inp = str(input("Enter the Key to get value:"))
obj = json.loads(user_obj)
#a_dict = {"a":{"b":{"c":"d"}}}
 
def iterate(dictionary,user_inp): 
    for key, value in dictionary.items(): 
        if isinstance(value, dict): 
            iterate(value,user_inp) 
            continue 
    #print('key {!r} -> value {!r}'.format(key, value)) 
    if key==user_inp:
        print(f'values is {value}')
 
iterate(obj,user_inp) 
 

