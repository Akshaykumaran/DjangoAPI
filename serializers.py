from rest_framework import serializers
from .models import Student,Books

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__' 