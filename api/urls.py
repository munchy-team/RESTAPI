from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MunchyList, MunchyAPI

urlpatterns = [
    path('munchy/', MunchyList.as_view()),
    path('mucnhy/<str:id>/', MunchyAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
