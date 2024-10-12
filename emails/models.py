from django.db import models

# Create your models here.
class Email(models.Model):
    sender = models.EmailField()
    email_text = models.TextField()
    is_phishing = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Blacklist(models.Model):
    sender = models.EmailField(unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

