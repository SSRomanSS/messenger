from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from ..models import Message
from . import serializers


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer


class PaginateListView(generics.ListAPIView):

    def get_queryset(self, **kwargs):
        n = int(self.kwargs['page_num']) * 10
        queryset = Message.objects.all()[n: n + 9]
        return queryset

    serializer_class = serializers.MessageSerializer


class MessagePost(APIView):

    def post(self, request):
        serializer = serializers.MessageSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('email')
            message = 'Hello! {}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleMessageGet(APIView):

    def get_object(self, pk):
        try:
            return Message.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404()

    def get(self, request, **kwargs):
        pk = kwargs['slug']
        message = self.get_object(pk=pk)
        serializer = serializers.MessageSerializer(message)
        return Response(serializer.data)
