from django.db import models

# Create your models here.
class Item(models.Model):
    
    # Django auto increment primary key
    record_id = models.AutoField()

    item_id = models.CharField(max_length=5, primary_key=True) 

    item_name = models.TextField()

    item_price = models.DecimalField(decimal_places=2)

    item_description = models.TextField()

    # Django auto timestamp creation of user (doens't update upon login)
    created_on = models.DateField(auto_now_add=True)
