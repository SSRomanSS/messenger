import re
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
        if request.method == 'POST':
            errors = {}
            data = {}
            reg_email = r'^\w+([!#$%&\'*+-/=?^_`{|}~]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
            reg_message = r'.*\S.*'
            email = data.get('email', '').strip()
            message = data.get('message')
            if not email or not re.match(reg_email, email):
                errors['email'] = 'input correct email'
            else:
                data['email'] = email
            if not message or not re.match(reg_message, message):
                errors['message'] = 'message cannot be empty'
            elif len(message) > 100:
                errors['message'] = 'message cannot be empty'
            else:
                data['message'] = message



            serializer = serializers.MessageSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
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
