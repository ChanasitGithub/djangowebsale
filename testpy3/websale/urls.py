from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='websale-home'),
                path('about/', views.about, name='websale-about'),
                path('blog/', views.blog, name='websale-blog'), 

            ]

