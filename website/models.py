from django.db import models

# Create your models here.


class Record(models.Model):
    # any time we create a new record django will give u timestamp on it
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        # what we show when we access one of these records
        # if u call one of the records in the admin area
        # or in a website, it will return First and Last name
        return (f'{self.first_name} {self.last_name}')
