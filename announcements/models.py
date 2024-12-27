from django.db import models

class Announcement(models.Model):
    file = models.FileField(upload_to='uploads/announcements/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=100)
    
    id_module = models.CharField(max_length=50)
    id_type = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'announcement'

class AnnouncementType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'announcement_type'

class AnnouncementModule(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'announcement_module'