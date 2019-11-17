from django.db import models

class Card(models.Model):
    url_suffix = models.CharField(max_length=50, default='')
    full_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=20, default='')
    bio_text = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.full_name
