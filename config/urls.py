from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.room.views import RoomViewSet

router = SimpleRouter()
router.register('room/filter_price', RoomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/booking/', include('apps.booking.urls')),
    path('api/', include(router.urls)),
    path('api/booking/', include('apps.booking.urls')),
    path('api/v1/account/', include('apps.account.urls')),
]
