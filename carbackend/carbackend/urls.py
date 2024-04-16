from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from car.views import CarViewSet, get_horsepowers, get_cars_by_horsepower

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('horsepowers/', get_horsepowers, name='horsepowers'),
        path('cars/horsepower/<int:horsepower>/', get_cars_by_horsepower, name='get_cars_by_horsepower'),
]