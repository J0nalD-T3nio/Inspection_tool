"""
URL configuration for inspection_tool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from . import views

APP_NAME = 'admin_pov'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login Page
    path('',include('inspection_tool.urls')),

    # Paths for the applications of each POV
    path('admin-pov', include('admin_pov.urls')),
    path('lead-pov', include('lead_pov.urls')),
    path('', include('inspector_pov.urls')),
]
