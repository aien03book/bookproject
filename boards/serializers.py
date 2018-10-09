from rest_framework import serializers
from boards.models import Members, Board, Post

class MembersSerialize(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class BoardSerialize(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class PostSerialize(serializers.ModelSerializer):
    boardname = serializers.ReadOnlyField(source='board.name')
    membername = serializers.ReadOnlyField(source='createdby.name')

    class Meta:
        model = Post
        fields = '__all__'

