from django.urls import path
from . import views

# TEMPLATE TAGGING
# app_name is keyword var. set it to application name
app_name = 'basic_app'

urlpatterns = [
    #path('',views.index,name='index'),
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
