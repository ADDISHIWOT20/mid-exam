from django.urls import path
from .views import employeList
from .views import employeDetail
from .views import employeupdate

urlpatterns = [
    path('employe-list/', employeList.as_view() ),
    path('employe/<int:pk>/', employeDetail.as_view() ),
    path('employe/<int:pk>/', employeupdate.as_view() ),

    
]