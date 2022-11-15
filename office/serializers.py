from rest_framework import serializers
from .models import OfficeResource,Employee,company

class PostSerializer(serializers.ModelSerializer):

    reasontobuy = serializers.CharField(max_length=200)
    class Meta:
        model = OfficeResource
        fields = ('name','employee','office','reasontobuy','issuedate','returndate')
        def get_fields(self, *args, **kwargs):
            fields = super( PostSerializer, self).get_fields(*args, **kwargs)
            request = self.context.get('request', None)
            if request and getattr(request, 'method', None) == "POST":
                fields['reasontobuy'].required = False
            return fields

class AddEmployeeSerializer(serializers.ModelSerializer):

    designation = serializers.CharField(max_length=200)
   
    class Meta:    
        model = Employee  
        fields = ['name','designation','company'] 
        extra_kwargs = {'company': {'required': True}}

    def get_fields(self, *args, **kwargs):
            fields = super( AddEmployeeSerializer, self).get_fields(*args, **kwargs)
            request = self.context.get('request', None)
            if request and getattr(request, 'method', None) == "POST":
                fields['designation'].required = False
                fields['company'].required = False
            return fields       
           

