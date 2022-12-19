from django.urls import path
from .views import Newsview

urlpatterns=[
    path('',Newsview.as_view(),name='news')
]