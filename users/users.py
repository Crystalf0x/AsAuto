from django.urls import path
from users.views import handle_login
from users.views import handle_logout

app_name = 'users'

urlpatterns = [path('login/', view=handle_login, name='login'),
               path('logout/', view=handle_logout, name='logout'),
               ]