from django.db import models

# Create your models here.
class Item(models.Model):
    
    # Django auto increment primary key
    record_id = models.AutoField(primary_key=True)

    item_id = models.CharField(max_length=5) 

    item_name = models.TextField()

    item_price = models.DecimalField(max_digits=10,decimal_places=2)

    item_description = models.TextField()

    item_available = models.IntegerField()

    photo = models.CharField(default='null', max_length=100 )


    # Django auto timestamp creation of user (doens't update upon login)
    created_on = models.DateField(auto_now_add=True)
