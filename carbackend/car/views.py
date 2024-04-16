from rest_framework import viewsets, pagination, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = StandardPagination


@api_view(['GET'])
def get_horsepowers(request):
    horsepowers = Car.objects.values_list('horsepower', flat=True).distinct()
    return Response(horsepowers)


@api_view(['GET'])
def get_cars_by_horsepower(request, horsepower):
    try:
        if horsepower == 0:
            cars = Car.objects.all()
        else:
            cars = Car.objects.filter(horsepower=horsepower)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)