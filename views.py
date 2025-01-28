from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from website.models import student
from website.serializer import LoginSerializer, StudentSerializer

# Create your views here.


def project(request):
    return render(request, 'form.html')



@api_view(["POST"])
def Student(request):
    response_details = {
        "status": False,
        "message": "Error happpend while processing",
        "status_code": 404,
        "data": []
    }

    if request.method == 'POST':
        received_data = StudentSerializer(data=request.data)
        if received_data.is_valid():
            student = received_data.save()
            return Response({
                "status": True,
                "status_code": 200,
                "message": "Data saved",
                "data": []
            })
    else:
        return Response(data={"message": received_data.errors})
    
    return Response(response_details)


@api_view(["POST"])
def Login(request):
    response_details = {
        "status": False,
        "message": "Error happpend while processing",
        "status_code": 404,
        "data": []
    }

    if request.method == "POST":
        received_data = LoginSerializer(data=request.data)
        if received_data.is_valid():
            user_name = request.data.get('user_name')
            password = request.data.get('password')
            Student = student.objects.filter(user_name=user_name,password=password).first()
            if Student:
                response_details.update({
                    "status": True,
                    "status_code": 200,
                    "message": "Login success",
                    "data": []
                })
            else:
                response_details.update({
                    "status": False,
                    "status_code": 400,
                    "message": "Invalid username or password",
                    "data": []
                })
        else:
            response_details.update({
                "message": received_data.errors
            })

    return Response(response_details)
            
