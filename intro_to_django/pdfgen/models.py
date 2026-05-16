from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="reports/", null=True, blank=True)
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)