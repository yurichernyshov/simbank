from django.urls import path
from .views import PingView, AddView, SubtractView, StatusView


app_name = 'api'

urlpatterns = [
    path('ping', PingView.as_view(), name='ping'),
    path('add', AddView.as_view(), name='add'),
    path('subtract', SubtractView.as_view(), name='subtract'),
    path('status', StatusView.as_view(), name='status'),
]
