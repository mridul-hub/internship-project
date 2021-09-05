from django.contrib import admin
from django.urls import path
from . import views
app_name = 'index'
urlpatterns = [
    path('signup',views.sign_up,name = 'signup'),
    path('login',views.login_view,name = 'login'),
    path('home/<slug:user_id>',views.home,name = 'home'),
    path('logout',views.logout_view,name = 'logout'),
    path('additem',views.additem_view,name = 'additem'),
    path('update/<slug:item_id>',views.update_view,name = 'updateitem'),
    path('filter/', views.filter_view, name="filter"),
    path('delete/<slug:item_id>', views.delete_view, name="delete"),
    path('edit/<slug:item_id>', views.edit,name="edit"),
]
