from django.shortcuts import render
from .models import OfficeResource
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from office.serializers import  AddEmployeeSerializer, PostSerializer
from rest_framework.views import  APIView
from django.shortcuts import get_object_or_404
from django.http import Http404
# Create your views here.

class ResourceOrder(APIView):

    def post(self,request):

        #if not request.data['reasontobuy']==None:

            serializer = PostSerializer(data=request.data)
            # print(request.data['reasontobuy'])
        

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

       #else:

           # return Response({"message":"give proper reason to buy "})


class AddEmployee(APIView):

    def post(self,request):

        serializer=   AddEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    




class ShowResource(APIView):

       def get(self,request,pk):

          
          queryset = OfficeResource.objects.filter(office=pk)
          def get_object(queryset):
            if queryset:
                pass
            else:
                raise Http404
          obj = get_object(queryset)
          data = OfficeResource.objects.filter(office=pk).values('name','employee','office','reasontobuy','issuedate','returndate')
          print(OfficeResource.objects.filter(office=pk).values('name','employee','office'))

          if not data == None:
             return Response(data)
          else:   
             return Response({"message":"data not found"})   