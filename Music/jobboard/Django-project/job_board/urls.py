from django.urls import include, path
from . import views

urlpatterns = [
     path('', views.landing_page, name='landing'),
    path('accounts/login/', views.custom_login, name='login'),
    path("home/", views.index, name="home"),
    path("job/<int:pk>/", views.job_detail, name="job-detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    
]
