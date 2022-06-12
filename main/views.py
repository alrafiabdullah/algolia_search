from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from algoliasearch_django import raw_search

from .models import Cars


# Create your views here.
class IndexView(APIView):
    def get(self, request):
        try:
            car_name = request.query_params["car_name"]
        except:
            return Response("Add a car_name parameter", status=status.HTTP_400_BAD_REQUEST)

        datetime_now = datetime.now()

        params = {"hitsPerPage": 5}
        response = raw_search(Cars, car_name, params)

        time_taken = (datetime.now() - datetime_now).total_seconds()

        data = {
            "time_taken": time_taken,
            "results": response,
        }

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # generate 1000 random cars
        for i in range(1000):
            Cars.objects.create(
                name="Car {}".format(i),
                cc=i,
                color="red",
                price=i,
            )

        return Response(status=status.HTTP_201_CREATED)
