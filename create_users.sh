#!/bin/bash
python3 manage.py shell
from Kiosk.models import Employee
user = Employee.objects.create(first_name='Andre',last_name='Fuentes', employee_id=12345, password=123, role='GM')
user.save()
user = Employee.objects.create(first_name='Ann',last_name='Frank', employee_id=11111, password=111, role='CS')
user.save()


