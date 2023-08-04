from datetime import datetime

from rest_framework import serializers


class CustomResponse:

    def __init__(self, data, is_error=False, message=None):
        self.data = data
        self.is_error = is_error
        self.message = message
        self.created = datetime.now()


class CustomResponseSerializer(serializers.Serializer):
    data = serializers.DictField()
    is_error = serializers.BooleanField(default=False)
    message = serializers.CharField()
    created = serializers.DateTimeField()
