from rest_framework import serializers
from .models import Tblemployeeprofile1

class Tblemployeeprofile1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tblemployeeprofile1
        fields = '__all__'