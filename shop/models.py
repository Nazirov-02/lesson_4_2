from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.category

class Discount(models.Model):
    number = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    value = models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return self.number
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"number: {self.number}"

    def apply_discount(self,price):
        return price * (1 - self.value / 100)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=14)
    stock = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discount = models.ForeignKey(Discount,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.name

    def final_discount(self):
        return self.discount.apply_discount(self.price)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user: {self.user.name}, product: {self.product.name}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user: {self.user.name}, product: {self.product.name}"

class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user: {self.user.name}, product: {self.product.name},rating: {self.rating}"


