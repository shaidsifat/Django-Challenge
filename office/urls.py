    
    

from django.urls import path,include
from .views import ResourceOrder,AddEmployee,ShowResource
urlpatterns = [
    
    path('Order/',ResourceOrder.as_view() , name='Resource'),
    path('addemployee/',AddEmployee.as_view(),name='addemployee'),
    path('ShowResource/<int:pk>',ShowResource.as_view(),name='ShowResource'),

]