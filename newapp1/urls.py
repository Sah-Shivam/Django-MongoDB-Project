from django.urls import path
# from .import views
from .views import PersonAPI

# urlpatterns = [
#     path('', views.index),
#     path('add/', views.add_person),
#     path('show/', views.get_all),
# ]

urlpatterns = [
    path('persons/', PersonAPI.as_view(), name='person-api'),
]

