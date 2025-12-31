from django.urls import path

from Recipe.views import ListApiView

urlpatterns = [
    path('list', ListApiView.as_view())
]