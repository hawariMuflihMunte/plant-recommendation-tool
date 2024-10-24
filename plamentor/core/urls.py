from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', view=views.index, name='home'),
    path('login/', view=views.login_view, name='login'),
    path('logout/', view=views.CustomLogoutView.as_view(), name='logout'),
]
