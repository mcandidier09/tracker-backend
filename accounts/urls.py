from django.conf.urls import url

from rest_framework.authtoken import views

from .views import (
    LoginView,
    LogoutView,
    DashboardView,
    SignupView,
)

from .api import AccountAPI, LoginAPI

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),

    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
]

signup_url = AccountAPI.as_view({'post': 'register'})
login_url = LoginAPI.as_view({'post': 'login'})
logout_url = LoginAPI.as_view({'post': 'logout'})

account_urlpatterns = [
    # user token
    url(r'^token/$', views.obtain_auth_token, name="token"),

    url(r'^signup/$', signup_url, name='register'),
    url(r'^login/$', login_url, name="user_login"),
    url(r'^logout/$', logout_url, name="user_logout"),
]