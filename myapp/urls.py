from django.urls import path

from myapp.views import login_view, MainView, CreateMemoryView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', MainView.as_view(), name='main'),
    path('create/', CreateMemoryView.as_view(), name='create'),
]
