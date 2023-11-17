
from django.urls import re_path
from .aliases import * 
from .views import *

from rest_framework_simplejwt.views import (
    token_obtain_pair,
    token_refresh,
    token_blacklist)


auth_paths = (
    re_path('^auth/login/?$', token_obtain_pair, name='api-login'),
    re_path('^auth/login/refresh/?$', token_refresh, name='api-login-refresh'),
    re_path('^auth/logout/?$', token_blacklist, name='api-logout'),)

user_paths = (
    re_path('^users/?$', UsersViewSet.as_view(LIST_CREATE), name='users-list'),
    re_path('^users/(?P<pk>\d+)/?$', UsersViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='user-detail'),)


urlpatterns = [
    *auth_paths,
    *user_paths,
]