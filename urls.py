from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name="Akki"),
    path('student/', views.StudentInfo, name='info'),
    path('books/', views.BookData, name='book'),
    path('student/list/', views.StudentList.as_view()),
    path('student/create/', views.StudentListCreate.as_view()),
    path('student/display/<int:pk>/', views.StudentListDisplay.as_view()),
    path('student/new/', views.StudentListApi.as_view()),
    path('student/create/api/', views.StudentCreateApi.as_view()),
]
