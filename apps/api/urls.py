from django.urls import path, include
from .views import home  # API home view

urlpatterns = [
    path('', home, name='api_home'),                # /api/
    path('users/', include('apps.users.urls')),    # /api/users/
    path('study/', include('apps.study.urls')),    # /api/study/
    path('payments/', include('apps.payments.urls')), # /api/payments/
]

