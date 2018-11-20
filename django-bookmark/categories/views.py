from categories.models import Category
from categories.serializers import CategorySerializer

from items.models import Item
from items.serializers import ItemSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def category_list(request, format=None):
    """List all code categories, or create a new category."""
    if request.method == 'GET':
        categories = Category.get_active()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def category_detail(request, pk, format=None):
    """Retrieve, update or delete a code category."""
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def category_search(request, pk, format=None):
    """Retrieve, update or delete a code category."""
    try:
        category = Category.objects.get(name=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        items = Item.get_active(category=category)
        print("items")
        serializer = ItemSerializer(items, many=True)
        # serializer = ItemsCategorySerializer(items, many=True)
        return Response(serializer.data)
