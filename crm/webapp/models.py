from django.db import models

# Customer Table

class Customer_Table(models.Model):
    customer_id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    customer_firstName = models.CharField(max_length=100)
    customer_lastName = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100, unique=True)
    customer_phone = models.CharField(max_length=15, unique=True)
    customer_address = models.TextField()
    customer_city = models.CharField(max_length=50)
    customer_state = models.CharField(max_length=50)
    customer_zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_firstName + " " + self.customer_lastName
