from django.db import models

class Announcement(models.Model):
    module = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'announcement'
