from django.urls import path
from core.views import login, logout, home, delete_contact, register_contact, edit_contact, show_contact


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('cadastrar/', register_contact , name='register_contact'),
    path('listar/', show_contact, name='show_contact'),
    path('editar/', edit_contact, name='edit_contact'),
    path('delete/', delete_contact, name='delete_contact'),
    path('', home,name='home')
]