from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Employee(models.Model):
    record_id = models.IntegerField(default= 0)

    first_name = models.TextField(default='team')

    last_name = models.TextField(default='five')

    employee_id = models.IntegerField(default=0)

    active = models.BooleanField(default=False)
    class Role(models.TextChoices):
        general_manager = 'GM', _('General Manager')
        shift_manager = 'SM', _('Shift Manager')
        cashier = 'CS', _('Cashier')

    role = models.CharField(max_length=2, choices= Role.choices, default=Role.cashier)


    password = models.TextField(default='teamfive')

    created_on = models.DateField(auto_now_add=True)


class Active_Employee(models.Model):
    
    record_id = models.IntegerField(default= 0)

    employee_id = models.IntegerField(default=0)

    name = models.TextField()

    class Role(models.TextChoices):
        general_manager = 'GM', _('General Manager')
        shift_manager = 'SM', _('Shift Manager')
        cashier = 'CS', _('Cashier')

    role = models.CharField(max_length=2, choices= Role.choices, default=Role.cashier)

    session_key = models.TextField()

    created_on = models.DateField(auto_now_add=True)


