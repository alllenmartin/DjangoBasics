from django.urls import path
from .views import GenericAPIViews

urlpatterns = [
    path('generic/article/', GenericAPIViews.as_view()),
    path('generic/details/<int:id>/', GenericAPIViews.as_view())
]
