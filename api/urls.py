
from django.urls import re_path
from .aliases import * 
from .views import *

from rest_framework_simplejwt.views import (
    token_blacklist)


auth_paths = (
    re_path('^auth/login/?$', LoginView.as_view(), name='api-login'),
    re_path('^auth/login/refresh/?$', LoginRefreshView.as_view(), name='api-login-refresh'),
    re_path('^auth/logout/?$', token_blacklist, name='api-logout'),)

user_paths = (
    re_path('^users/?$', UsersViewSet.as_view(LIST_CREATE), name='users-list'),
    re_path('^users/(?P<pk>\d+)/?$', UsersViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='user-detail'),)


urlpatterns = [
    *auth_paths,
    *user_paths,
]