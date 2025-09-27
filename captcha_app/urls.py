from django.urls import path
from .views import login_view, signed_in_view

urlpatterns = [
    path('', login_view, name='login'),
    path('signed-in/', signed_in_view, name='signed_in'),
]
