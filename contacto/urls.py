from django.urls import path
from .views import PersonasView, TelefonosView, EmailsView

urlpatterns = [
    path('persona/', PersonasView.as_view(), name='personas-list'),
    path('persona/<int:numero_documento>/', PersonasView.as_view(), name='personas-list-detail'),
    path('telefono/', TelefonosView.as_view(), name='edit-telefonos'),
    path('telefono/<int:id>/', TelefonosView.as_view(), name='delete-telefonos'),
    path('email/', EmailsView.as_view(), name='edit-emails'),
    path('email/<int:id>/', EmailsView.as_view(), name='delete-emails')
]