# -*- coding: utf-8 -*-

import re
from rest_framework import serializers
from ..models import Message

# TODO to find solution, why validators not works


def custom_email_validator(data):
    """
    Check that email is correct.
    """

    reg_email = r'^\w+([!#$%&\'*+-/=?^_`{|}~]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
    email = data.get('email')
    if not email or not re.match(reg_email, email):
        raise serializers.ValidationError({"email": "email is incorrect"})
    return data


def custom_message_validator(data):
    """
    Check that message is not empty.
    """

    reg_message = r'.*\S.*'
    message = data.get('message')
    if not message or not re.match(reg_message, message):
        raise serializers.ValidationError({"message": "message is empty"})
    return data


def message_length_validator(data):
    """
    Check that message is less then 100 symbols
    """

    message = data.get('message')
    if len(message) > 100:
        raise serializers.ValidationError({"message": "message is more 100 symbols"})
    return data


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message Model
    """
    class Meta:
        model = Message
        fields = ('email', 'message', 'time_create', 'time_update')
        validators = [
            custom_email_validator,
            custom_message_validator,
            message_length_validator
        ]
