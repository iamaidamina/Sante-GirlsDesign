from rest_framework import status, views
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.psSerializer import PsSerializer
class PsCreateView(views.APIView):
    def post(self, request, *args):
        serializer = PsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {
            "User_id":request.data["User_id"],
            "nombre":request.data["nombre"],
            "apellido":request.data["apellido"],
            "tipo_documento":request.data["tipo_documento"],
            "numero_documento":request.data["numero_documento"],
            "fecha_nacimiento":request.data["fecha_nacimiento"],
            "genero":request.data["genero"],
            "telefono ":request.data["telefono"],
            "correo_electronico":request.data["correo_electronico"],
            "registro ":request.data["registro"],
            "especialidad_id":request.data["especialidad_id"],}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return "Creado Correctamente"
