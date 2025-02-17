from django.urls import path

from .views import (
    CreateUserView, VerifyAPIView, GetNewVerification, \
    UpdateUserInformationView, UpdateUserPhotoView, LoginView, LoginRefreshView, \
    LogOutView, ForgotPasswordView, ResetPasswordView
)

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('login/refresh', LoginRefreshView.as_view(), name='login-refresh'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('signup', CreateUserView.as_view(), name='signup'),
    path('verify', VerifyAPIView.as_view(), name='verify'),
    path('verify/new', GetNewVerification.as_view(), name='new-verify'),
    path('', UpdateUserInformationView.as_view(), name='update-user'),
    path('photo', UpdateUserPhotoView.as_view(), name='update-user-photo'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password', ResetPasswordView.as_view(), name='reset-password'),
]