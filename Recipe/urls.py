from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Recipe import views

router = DefaultRouter()
router.register('view-set', views.BaseViewSet, basename='view-set')
router.register('profile-set', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemView)

urlpatterns = [
    path('list', views.ListApiView.as_view()),
    path('', include(router.urls)),
    path('login', views.UserLoginApiView.as_view())
]