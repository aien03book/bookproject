from rest_framework import serializers
from .models import Todo
from home.models import Bookpool
from home.models import Bookcate

class BookpoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookpool
        fields = '__all__'

class BookcateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookcate
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'