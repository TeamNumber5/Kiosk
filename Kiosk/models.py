from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Employee(models.Model):
    
    # Django auto increment primary key
    record_id = models.AutoField(primary_key=True)

    first_name = models.TextField()

    last_name = models.TextField()

    employee_id = models.CharField(max_length=5)

    # States whether the user is active or inactive.
    active = models.BooleanField(default=False)

    # Object for choices of role
    class Role(models.TextChoices):
        general_manager = 'GM', _('General Manager')
        shift_manager = 'SM', _('Shift Manager')
        cashier = 'CS', _('Cashier')

    role = models.CharField(max_length=2, choices= Role.choices, default=Role.cashier)

    manager = models.IntegerField(blank=True, null=True)

    password = models.TextField()

    # Django auto timestamp creation of user (doens't update upon login)
    created_on = models.DateField(auto_now_add=True)


class Active_Employee(models.Model):
    
    # Django auto increment primary key
    record_id = models.AutoField(primary_key=True)

    employee_id = models.CharField(max_length=5)

    name = models.TextField()

    class Role(models.TextChoices):
        general_manager = 'GM', _('General Manager')
        shift_manager = 'SM', _('Shift Manager')
        cashier = 'CS', _('Cashier')

    role = models.CharField(max_length=2, choices= Role.choices, default=Role.cashier)

    # Holds the session key generated from login request
    session_key = models.TextField()

    # Creates a timestamp of when a employee login
    created_on = models.DateField(auto_now_add=True)


