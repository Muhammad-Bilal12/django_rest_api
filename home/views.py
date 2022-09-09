from email import message
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.serializer import TodoSerializer
from .models import Todo

# Create your views here.

@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'Yes! Django rest framework start!',
            'method' : 'Calling GET'
    })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'Yes! Django rest framework start!',
            'method' : 'Calling POST'
    })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': 'Yes! Django rest framework start!',
            'method' : 'Calling PATCH'
    })
    else :
        return Response({
            'status': 400,
            'message': 'Yes! Django rest framework start!',
            'method' : 'INVALID'
    })


@api_view(['GET'])
def get_todo(request):
    todo_obj = Todo.objects.all()
    serializer = TodoSerializer(todo_obj,many = True)

    return Response(
        {
            'status': 200,
            'message':"Todo Fetched",
            'data': serializer.data
        }
    )


@api_view(['POST'])
def postTodo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(data)
            return Response({
                'status': True,
                'message': 'Success data',
                'data' : serializer.data
        })
     
        return Response({
            'status': False,
            'message': 'Invalid data',
            'data' : serializer.errors
    })

    except Exception as e:
        print(e)    
        return Response({
            'status': False,
            'message': 'Some error occured',
    })
