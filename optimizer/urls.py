from django.urls import path
from . import views

urlpatterns = [

    path('dashboard', views.dashboard, name='dashboard'),
    # create website
    path('createwebsite', views.createwebsite, name='createwebsite'),
    # view website
    path('viewwebsite/<int:id>', views.viewwebsite, name='viewwebsite'),
    # optimize website
    path('optimize/<int:id>', views.optimize, name='optimize'),
    # delete website
    path('delete/<int:id>', views.delete_website, name='delete_website'),
    
 ]