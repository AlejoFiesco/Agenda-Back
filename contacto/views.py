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
        
    def post(self, request):
        personaData = request.data.get('persona', {})
        telefonoData = request.data.get('telefono', {})
        emailData = request.data.get('email', {})
        personaSerializer = PersonaSerializer(data = personaData)
        telefonoSerializer = TelefonoSerializer(data = telefonoData)
        emailSerializer = EmailSerializer(data=emailData)

        if personaSerializer.is_valid():
            persona = personaSerializer.save()
            if telefonoSerializer.is_valid():
                telefonoSerializer.save(persona=persona)
            if emailSerializer.is_valid():
                emailSerializer.save(persona=persona)
            return Response(personaSerializer.data, status=status.HTTP_200_OK)
        return Response(personaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, numero_documento=None):
        if(numero_documento == None): return(Response('Este número de documento no existe', status=status.HTTP_400_BAD_REQUEST))        
        
        try:
            persona = Personas.objects.get(numero_documento = numero_documento)
            persona.delete()
            return Response('Contacto eliminado', status=status.HTTP_204_NO_CONTENT)
        except Personas.DoesNotExist:
            return Response('Este contacto no existe', status=status.HTTP_404_NOT_FOUND)

            


class TelefonosView(APIView):
    def post(self, request):
        serializer = TelefonoSerializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:

            print(serializer.errors)
        return Response('Se enviaron datos incorrectos', status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request, id=None):
        if(id == None): return(Response('Este número de telefono no existe', status=status.HTTP_400_BAD_REQUEST))        
        
        try:
            telefono = Telefono.objects.get(id = id)
            telefono.delete()
            return Response('Telefono eliminado', status=status.HTTP_204_NO_CONTENT)
        except Telefono.DoesNotExist:
            return Response('Este telefono no existe', status=status.HTTP_404_NOT_FOUND)

class EmailsView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Se enviaron datos incorrectos', status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request, id=None):
        if(id == None): return(Response('Este número de telefono no existe', status=status.HTTP_400_BAD_REQUEST))        
        
        try:
            telefono = Personas.objects.get(id = id)
            telefono.delete()
            return Response('Telefono eliminado', status=status.HTTP_204_NO_CONTENT)
        except Personas.DoesNotExist:
            return Response('Este telefono no existe', status=status.HTTP_404_NOT_FOUND)

    