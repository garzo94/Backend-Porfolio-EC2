from django.shortcuts import render
from backend.models import DataCard
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.serializers import DataCardSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
# AUTENTICACION
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated 


from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class DataCardApiView(APIView,PageNumberPagination):
    authentication_classes = [BasicAuthentication] 
    permission_classes = [IsAuthenticated] 

    def get(self, request, type="all"):
        print("que pedo??")
        if type == 'all':
            queryset = DataCard.objects.all()
        else:
            queryset = DataCard.objects.filter(appType=type)
        
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = DataCardSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

        # permission_classes = [permissions.IsAdminUser]
class send_emails(APIView):

    def post(self,request):

        message = request.data['message']
        email = request.data['email']
        name = request.data['name']
        print(message,'requestttt')

        send_mail(
            'Contact from portfolio',
            message + f'\n\n Nombre: {name}' + f'\n Email: {email}',
            settings.EMAIL_HOST_USER, #from
            ["alexgarzo25@gmail.com"], # to
            fail_silently=False)

        return Response({'status':'email success send'})

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})