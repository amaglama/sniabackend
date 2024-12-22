from django.db import models

class Rentraa(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'test'