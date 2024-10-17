from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('details/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
