from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=90)

    # Contact
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    suburb = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=90, blank=True, null=True)
    state = CountryField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = ('name', 'email', 'suburb')

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.email, self.suburb)
