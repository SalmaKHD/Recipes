from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Recipe import views

router = DefaultRouter()
router.register('view-set', views.BaseViewSet, basename='view-set')
urlpatterns = [
    path('list', views.ListApiView.as_view()),
    path('', include(router.urls))
]