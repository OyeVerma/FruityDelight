from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path

from FruityDelightApp.views import ComplaintView, AboutUs, AboutTeam, ComplaintView, GetFruity, Landpage, Ordered, SeeOrders, Waiting, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Landpage.as_view(), name="landpage"),
    path('get/<str:order>/', GetFruity.as_view(), name='getFruity'),
    path('order/', Ordered.as_view(), name="order"),
    path('order/<int:id>/waiting/', Waiting.as_view(), name="waiting"),
    path('orders/', SeeOrders.as_view(), name="seeorders"),
    path('aboutus/', AboutUs.as_view(), name="aboutus"),
    path('aboutTeam/', AboutTeam.as_view(), name="aboutteam"),
    path('complaint/', ComplaintView.as_view(), name="complaint"),
    path('logout/', logout_user, name="logout")
]
