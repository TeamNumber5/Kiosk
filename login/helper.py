from Kiosk.models import Employee
from Kiosk.models import Active_Employee
import json

import random
import string

"""
Every time the login page is loaded we update users.txt
this allows us to see who is the the employee database
without having to do queries
"""
def create_usertxt():
    with open('users.txt', 'w') as user:
        users = Employee.objects.all()
        for item in users:
            print ('-' * 40, file=user)
            print ('first_name '.ljust(15, ' ') + str(item.first_name),file=user)
            print ('last_name '.ljust(15, ' ') + str(item.last_name),file=user)
            print ('employee_id '.ljust(15, ' ') + str(item.employee_id),file=user)
            print ('password '.ljust(15, ' ') + str(item.password), file=user)
            print ('role '.ljust(15, ' ') + str(item.role),  file=user)

"""
Returns true if the employee id is unique
false otherwise
"""
def unique_id(employee_id):
    is_unique = True
    users = Employee.objects.all()
    # Checks if user ID is already taken
    for user in users:
        if employee_id == int(user.employee_id):
            is_unique = False

    return is_unique

"""

"""
def validate_create_user(first_name, last_name,employee_id, user_password, role):
    valid = True

    if not first_name.isalpha() or first_name == '' or not last_name.isalpha() or last_name == '':
        valid = False
    if len(str(employee_id)) != 5 or not unique_id(employee_id):
        valid = False
    if user_password == "":
        valid = False
    if role != 'GM' and role != 'SM' and role != 'CS':
        valid = False
    return valid


def create_user(first_name, last_name, employee_id, user_password, role):
        employee = Employee.objects.create(first_name=first_name,last_name=last_name, employee_id=employee_id, password=user_password, role=role)
        if role == 'GM' or role == 'SM':
            employee.manager = employee_id
        employee.save()





def attempt_create_user(form, context): 
    employee_id = 0
    first_name = ""
    last_name = ""
    role = ""
    user_password = ""
    try:
        first_name =str(form['first_name'].value())
        last_name = str(form['last_name'].value())
        user_password= str(form['user_password'].value())
        employee_id = int(form['employee_id'].value())                
        role = str(form['role'].value())
    except:
        context['valid_info'] = 0


    if validate_create_user(first_name, last_name, employee_id, user_password, role):
        create_user(first_name, last_name, employee_id, user_password, role)
    else:
        context['valid_info'] = 0

def get_user(employee_id, user_password):
    return(Employee.objects.filter(employee_id=employee_id,  password=user_password).first())



def attempt_login(request,user,context):
    if user:
        session_key = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        name = user.first_name
        employee_id = user.employee_id
        role = user.role
       
        """
        This is just checking to see if user is already logged in and didn't log out
        """
        active = Active_Employee.objects.filter(employee_id=employee_id).first()

        if active:
            remove_user(active)
        
        active_employee = Active_Employee.objects.create(employee_id=employee_id, name=name, role=role, session_key=session_key)
        active_employee.save()

        request.session['session_key'] = session_key
        print(request.session['session_key'])
        # If so direct them to the menu
        return True
    else:
        context['invalid_login'] = ''
        return False


def remove_user(user):
    try:
        user.delete()
    except:
        pass

def empty_db(context):
    users = Employee.objects.all()
    if len(users) == 0:
        context['no_users']= 1