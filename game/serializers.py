from game.models import Game
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    owner_name = serializers.CharField(source='owner.username', read_only=True)

    class Meta: 
        model = Game
        exclude = ['category', 'owner',]
    
    def get_category_name(self, instance):
        return instance.get_category_display()