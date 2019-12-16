from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from models.client.models import Client
from .serializers import ClientSerializer


class ClientView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'client/list.html'
    permission_classes = (AllowAny,)

    def get(self, request):
        # Know how to do server side, but this was quick for presentation. :)
        qv_client = Client.objects.all()
        return Response({'clients': qv_client})


class ClientCreateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'client/create.html'
    permission_classes = (AllowAny,)

    def get(self, request):
        serializer = ClientSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/')


class ClientEditView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'client/edit.html'
    permission_classes = (AllowAny,)

    def get(self, request, client_id):
        client = get_object_or_404(Client, pk=client_id)
        serializer = ClientSerializer(client)
        return Response({'serializer': serializer, 'client': client})

    def post(self, request, client_id):
        client = get_object_or_404(Client, pk=client_id)
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'client': client})
        serializer.save()
        return redirect('/')
