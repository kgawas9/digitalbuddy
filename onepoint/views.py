import imp
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import NewJoinerDetails
# Create your views here.

class NewJoinerGradeView(APIView):
    def get(self, request, PSID=None, format=None):
        empid = PSID
        print(empid)
        if empid is not None:
            try:
                emp = NewJoinerDetails.objects.values_list('grade', flat=True).filter(PSID=empid)
                return Response({'Your grade is': emp[0]})
            except:
                return Response({'msg':'No data found'}, status= status.HTTP_204_NO_CONTENT)

        res = {'msg':'No record found'}
        return Response(res, status = status.HTTP_204_NO_CONTENT)


class JoiningDateView(APIView):
    def get(self, request, PSID=None, format=None):
        emp_id = PSID

        if emp_id is not None:
            try:
                emp = NewJoinerDetails.objects.values_list('date_of_joining', flat=True).filter(PSID=emp_id)

                return Response({'Your date of joining is': emp[0]})
            except:
                return Response({'msg':'Employee is not found in database'}, status=status.HTTP_204_NO_CONTENT)

        res = {'msg':'No record found'}
        return Response(res, status = status.HTTP_204_NO_CONTENT)