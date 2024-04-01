from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import Blog, Student, Books
from .serializers import StudentSerializer, BooksSerializers
from rest_framework.generics import GenericAPIView, ListAPIView,CreateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin
# Create your views here.
@api_view(["GET"])
def home(request):
    post = Blog.objects.all()
    context = {'post':post}
    return Response({'status':200,})

@api_view(['GET', 'POST'])
def StudentInfo(request):
    student = Student.objects.all()
    stud = StudentSerializer(student, many=True)
    return Response({'status':200, 'payload':stud.data})

@api_view(['POST',])
def BookData(request): 
    book = Books.objects.all()
    serializer = BooksSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({serializer.data})

class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request):
        return self.list(request)
    
class StudentListCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self, request):
        return self.create(request)
    
class StudentListDisplay(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)
    
class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateApi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer