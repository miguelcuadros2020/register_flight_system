def validation_generic(type_var:any, text_person:str = None, conditions:list [any]= [lambda x:True], value_n:any = None)->any:

    extin_while:bool = True #flag of the while
    while extin_while:
        try:

            flag_value:bool = True #flag of the if or of the value_n
            if value_n == None:
                flag_value = False
                value_n = type_var(input(f"\n{text_person}"))

            flag:bool = True #flag of the for
            for condition in conditions: #validation of the conditions
                if not condition(value_n):
                    flag = False
                    break

            #return or extin for input of the users
            if not flag_value:
                if flag:
                    extin_while = False
                    result:any = type_var(value_n)
                else:
                    value_n = None
                    raise ValueError
                continue
            
            # return or extin for value_n
            if not flag:
                result:any = False
            else:
                result:any = True
            
            extin_while = False
                
        except ValueError:
            print("\nValue invalid, please try again.\n")
     # return       
    return result