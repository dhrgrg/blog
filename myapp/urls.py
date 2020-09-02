from django.urls import path
from myapp.views import index,PostCreate,detail,like

app_name = 'myapp'

urlpatterns = [
    path('',index,name = 'index'),
    path('create/',PostCreate.as_view(),name = 'create'),
    path('detail/<int:pk>/',detail,name = 'detail'),
    path('ajax/likes/',like,name = 'like'),
]