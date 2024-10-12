from rest_framework import serializers
from .models import Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ["id","sender","email_text","is_phishing","created_at"]