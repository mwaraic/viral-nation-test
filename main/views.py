from rest_framework.views import APIView
from rest_framework.response import Response
from main.functions import fetch_and_store_users, get_product
from main.utils.pg import Pg
from main.utils.mongo import Mongo
from main.serializers import CountSerializer
from rest_framework import status

class Count(APIView):

    def post(self, request):

        serializer = CountSerializer(data=request.data)
        
        if serializer.is_valid():
            count = request.data.get('count')
            for i in range(count):
                fetch_and_store_users.delay(i)
            return Response(status=200)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": serializer.errors})

class PGData(APIView):

    def get(self, request):

        pg_obj = Pg()
        data = pg_obj.retrieve_data()
        return Response(status=200, data=data)


class MongoData(APIView):

    def get(self, request):

        mongo_obj = Mongo()
        data = mongo_obj.retrieve_data()
        return Response(status=200, data=data)
    
class ProductData(APIView):

    def get(self, request, product_id):
        
        data = get_product(product_id)
        return Response(status=200, data=data)
    

