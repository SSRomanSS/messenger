# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from ..models import Message
from . import serializers


class MessageListView(generics.ListAPIView):
    """
    GET all messages from
    /api/messages/list/
    """

    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer


class PaginateListView(generics.ListAPIView):
    """
    GET messages pagination by 10 messages per request from
    /api/messages/list/'page_num'
    'page_num' 0 return messages 1-10, etc
    """

    def get_queryset(self, **kwargs):
        number = int(self.kwargs['page_num']) * 10
        queryset = Message.objects.all()[number: number + 9]
        return queryset

    serializer_class = serializers.MessageSerializer


class MessagePost(APIView):
    """
    POST method for creating a new message on
    /api/messages/post_message/
    """

    def post(self, request):
        if request.method == 'POST':

            serializer = serializers.MessageSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleMessageGet(APIView):
    """
    GET method for getting single message by unique identifier
    /api/messages/single/unique_message_identifier(Primary Key in a database)
    """

    def get_object(self, pk):
        """
        Override for getting single message by pk
        """
        try:
            return Message.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404()

    def get(self, request, **kwargs):  # used overrided get_object() for getting single message
        pk = kwargs['slug']
        message = self.get_object(pk=pk)
        serializer = serializers.MessageSerializer(message)
        return Response(serializer.data)
