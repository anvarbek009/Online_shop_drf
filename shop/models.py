from django.db import models
from users.models import User
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Categories"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Products"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name}--{self.product.name}'