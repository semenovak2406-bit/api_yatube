from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

comments_router = DefaultRouter()
comments_router.register(
    r'posts/(?P<post_pk>\d+)/comments', 
    CommentViewSet, 
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('v1/', include(router.urls)),
    path('v1/', include(comments_router.urls)),
]