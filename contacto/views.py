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
    
    def put(self, request, numero_documento = None):
        if(not numero_documento): Response('No se ha encontrado esta persona', status=status.HTTP_400_BAD_REQUEST)
        try:
            persona = Personas.objects.get(numero_documento = numero_documento)
        except Personas.DoesNotExist:
            return Response('No se encontro la persona', status=status.HTTP_404_NOT_FOUND)
        serializer = PersonaSerializer(persona, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, numero_documento=None):
        if(numero_documento == None): return(Response('Este número de documento no existe', status=status.HTTP_400_BAD_REQUEST))        
        
        try:
            persona = Personas.objects.get(numero_documento = numero_documento)
            persona.delete()
            return Response('Contacto eliminado', status=status.HTTP_204_NO_CONTENT)
        except Personas.DoesNotExist:
            return Response('Este contacto no existe', status=status.HTTP_404_NOT_FOUND)

            


class TelefonosView(APIView):
    def get(self, request, id=None):
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

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
        except Telefono.DoesNotExist:
            return Response('Este telefono no existe', status=status.HTTP_404_NOT_FOUND)
        
        telefono.delete()
        return Response('Telefono eliminado', status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id = None):
        if(id): 
            try:
                telefono = Telefono.objects.get(id = id)
            except Telefono.DoesNotExist:
                return Response('No se encontro el telefono', status=status.HTTP_404_NOT_FOUND)
            serializer = TelefonoSerializer(telefono, data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            Response('No se ha encontrado este telefono', status=status.HTTP_400_BAD_REQUEST)
class EmailsView(APIView):
    def get(self, request, id=None):
        return Response(status = status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = EmailSerializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Se enviaron datos incorrectos', status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request, id=None):
        if(id == None): return(Response('Este email no existe', status=status.HTTP_400_BAD_REQUEST))        
        
        try:
            telefono = Email.objects.get(id = id)
        except Email.DoesNotExist:
            return Response('Este email no existe', status=status.HTTP_404_NOT_FOUND)
        
        telefono.delete()
        return Response('Email eliminado', status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id = None):
        if(not id): Response('No se ha encontrado este email', status=status.HTTP_400_BAD_REQUEST)
        try:
            email = Email.objects.get(id = id)
        except Email.DoesNotExist:
            return Response('No se encontro el email', status=status.HTTP_404_NOT_FOUND)
        serializer = EmailSerializer(email, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    