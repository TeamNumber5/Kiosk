from django import forms

class ResetDB(forms.Form):
    pass

class logout(forms.Form):
    pass


class CreateProduct(forms.Form):
    product_name =   forms.CharField(label='product_name', max_length=100)
    product_desc =   forms.CharField(label='product_desc', max_length=400)
    product_price =  forms.CharField(label='product_price',max_length=100)
    product_qavail = forms.CharField(label='product_qavail', max_length=100)

class UpdateProduct(forms.Form):
    product_id =     forms.CharField(label='product_id', max_length=5)
    product_name =   forms.CharField(label='product_name', max_length=100)
    product_desc =   forms.CharField(label='product_desc', max_length=400)
    product_price =  forms.CharField(label='product_price',max_length=100)
    product_qavail = forms.CharField(label='product_qavail', max_length=100)

class GoUpdate(forms.Form):
    product_id =     forms.CharField(label='product_id', max_length=5)

class DeleteProduct(forms.Form):
    product_id =     forms.CharField(label='product_id', max_length=5)
