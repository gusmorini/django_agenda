from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # contact
    path('<int:contact_id>/', views.contact, name='contact'),
    path('<int:contact_id>/update/', views.update, name='update'),
    path('<int:contact_id>/delete/', views.delete, name='delete'),
    path('create', views.create, name='create'),
    path('search', views.search, name='search'),
    path('', views.index, name='index'),
    # user
    path('user/register', views.register, name='register'),
    path('user/login', views.login_view, name='login'),
    path('user/logout', views.logout, name='logout'),
]
