from rest_framework.decorators import api_view
from rest_framework.response import Response

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
            'status': 200,
            'message': 'Yes! Django rest framework start!',
            'method' : 'INVALID'
    })
