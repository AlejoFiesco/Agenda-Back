from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Personas, Email, Telefono
from .serializers import PersonaSerializer, EmailSerializer, TelefonoSerializer

class PersonasView(APIView):
    def get(self, request, numero_documento=None):
        if(numero_documento):
            try:
                persona = Personas.objects.get(numero_documento = numero_documento)
                serializer = PersonaSerializer(persona)
                return(Response(serializer.data, status= status.HTTP_200_OK))
            except Personas.DoesNotExist:
                return(Response('Esta persona no existe', status=status.HTTP_400_BAD_REQUEST))                
        else:
            personas = Personas.objects.all()
            serializer = PersonaSerializer(personas, many=True)
            responseData = {
                'personas': serializer.data
            }
            return Response(responseData, status = status.HTTP_200_OK)

class TelefonosView(APIView):
    def post(self, request):
        print(request.data)
        serializer = TelefonoSerializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        return Response('Se enviaron datos incorrectos', status=status.HTTP_400_BAD_REQUEST)    
class EmailsView(APIView):
    def post(self, request):
        print(request.data)
        serializer = EmailSerializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Se enviaron datos incorrectos', status=status.HTTP_400_BAD_REQUEST)    
    