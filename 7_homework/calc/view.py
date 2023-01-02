def view_data(data):
    print(f'sum = {data}')

def get_numbers():
    var_numbers=input('choose complex or rational numbers ')
    if var_numbers=='rational': return True
    elif var_numbers=='complex': return False
    else: return 'Error choose complex or rational numbers'

def fraction_name():
    f_name = input('Does the number are fraction? print y/n ')
    if f_name=='y': return False
    elif f_name=='n': return True
    else: print('Error choose fraction')

def get_operation():
    operation_name=input('Write operation: ')
    if operation_name=='+': return 'sum'
    elif operation_name=='-': return 'minus'
    elif operation_name=='*': return 'mult'
    elif operation_name=='/': return 'div'
    else: return 'Error operation name '

def get_value():
    return int(input('value = '))
