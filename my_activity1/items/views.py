from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_items(request):
    """Retrieve all items, with optional search filtering."""
    search_query = request.GET.get('search', None)
    if search_query:
        items = Item.objects.filter(name__icontains=search_query)
    else:
        items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_item(request):
    """Add a new item dynamically to the database."""
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Item added successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_item(request, item_id):
    """Retrieve a specific item by ID."""
    try:
        item = Item.objects.get(id=item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_item(request, item_id):
    """Update an existing item dynamically."""
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data, partial=True)  # ✅ Allows partial updates
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Item updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request, item_id):
    """Delete an item dynamically."""
    try:
        item = Item.objects.get(id=item_id)
        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
