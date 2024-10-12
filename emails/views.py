from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Email, Blacklist
from .serializers import EmailSerializer
from .model_predict import predict_email


# Create your views here.
class EmailViewSet(viewsets.ViewSet):
    def create(self, request):
        sender = request.data.get('sender')
        email_text = request.data.get('email_text')

        blaclisted = Blacklist.objects.filter(sender = sender).exists()

        if blaclisted:
            return Response(
                {"message":f"The sender {sender} is blacklisted already."},
                status = status.HTTP_403_FORBIDDEN
            )

        is_phishing = predict_email(email_text)

        email = Email.objects.create(sender=sender, email_text=email_text, is_phishing=is_phishing)

        if is_phishing:
            Blacklist.objects.get_or_create(sender=sender)

        serializer = EmailSerializer(email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)