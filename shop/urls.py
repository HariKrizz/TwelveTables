from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='home'),
    path('<slug:c_slug>/',views.homePage,name='pct_home'),
    path('<slug:c_slug>/<slug:p_slug>',views.prd_details,name='details'),
    path('search',views.search,name='search'),
]