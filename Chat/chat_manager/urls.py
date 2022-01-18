from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='index_page'),

    path('auth/', LoginUser.as_view(), name='auth'),
    path('logout/', logout_user, name='logout'),

    path('room/<int:room_id>', room, name='room'),

    # path('send_msg', send_msg, name='send_msg')
]