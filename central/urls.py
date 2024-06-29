from django.contrib import admin
from django.urls import include, path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', include('mainapp.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
