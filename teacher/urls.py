from django.urls import path
from .views import teacherList
from .views import teacherDetail
from .views import teacherupdate

urlpatterns = [
    path('teacher-list/', teacherList.as_view() ),
    path('teacher/<int:pk>/', teacherDetail.as_view() ),
    path('teacher/<int:pk>/', teacherupdate.as_view() ),

    
]