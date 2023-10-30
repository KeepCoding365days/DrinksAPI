from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_400_BAD_REQUEST


@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method=='GET':
        drinks= Drink.objects.all()
        serializer= DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':serializer.data})
    
    if request.method=='POST':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
    if request.method=='GET':
        drink= Drink.objects.get(pk=id)
        serializer=DrinkSerializer(drink)
        return JsonResponse(serializer.data)
    
    elif request.method=='PUT':
        drink=Drink.objects.get(pk=id)
        serializer=DrinkSerializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        drink= Drink.objects.get(pk=id)
        serializer=DrinkSerializer(drink)
        drink.delete()
        return Response(serializer.data,status=HTTP_200_OK)