
from django.urls import re_path
from .aliases import * 
from .views import *


auth_paths = (
    re_path('^auth/login/?$', LoginView.as_view(), name='api-login'),
    re_path('^auth/login/refresh/?$', LoginRefreshView.as_view(), name='api-login-refresh'),
    re_path('^auth/logout/?$', LogoutView.as_view(), name='api-logout'),)

user_paths = (
    re_path('^users/?$', UsersViewSet.as_view(LIST_CREATE), name='users-list'),
    re_path('^users/(?P<pk>\d+)/?$', UsersViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='user-detail'),)

product_paths = (
    re_path('^products/?$', ProductsViewSet.as_view(LIST_CREATE), name='products-list'),
    re_path('^products/(?P<pk>\d+)/?$', ProductsViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='product-detail'),)


urlpatterns = [
    *auth_paths,
    *user_paths,
    *product_paths,
]