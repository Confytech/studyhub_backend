from django.contrib import admin
from django.urls import path, include
from apps.study.views import home  # Import the homepage view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Homepage route
    path('api/', include('apps.api.urls')),  # Added this line for the api app
    path('api/users/', include('apps.users.urls')),
    path('api/study/', include('apps.study.urls')),
    path('api/payments/', include('apps.payments.urls')),
]

