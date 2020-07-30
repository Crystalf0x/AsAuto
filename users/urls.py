from django.urls import path
from users.views import register, handle_login, handle_logout, profile, upload, profile_email
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
    path('login/', view=handle_login, name='login'),
    path('logout/', view=handle_logout, name='logout'),
    path('profile/', view=profile, name='profile'),
    path('profile/email', view=profile_email, name='profile_email'),
    path('register/', view=register, name='register'),
    path('upload/', view=upload, name='upload'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]

url_patterns=[


    url(r'^favicon\.ico$',RedirectView.as_view(url='/media/property_picture/30813999_1930164200350238_7978147448132520828_o.jpg')),
]