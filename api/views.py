from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from api.serializers import StudentsSerializer
from students.models import Students
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def studentsViews(request):
    if request.method == "GET":
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = StudentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
def studentDetailsViews(request ,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentsSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =="POST":
        serializer = StudentsSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






















