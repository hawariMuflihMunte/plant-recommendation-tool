from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', view=views.index, name='home'),
    path('login/', view=views.login_view, name='auth_login'),
]
