from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import *
from vgh.models import Profile

class AchievementSerializer(ModelSerializer):
    game = ReadOnlyField(source="game.title")
    class Meta:
        model = Achievement
        fields = ['id','title','description','difficulty','game']

class ProfileSerializer(ModelSerializer):
    user = ReadOnlyField(source="user.username")
    class Meta:
        model = Profile
        fields = ['user','news_letter','level','total_xp','missing_xp','profile_pic']

class GameSaveSerializer(ModelSerializer):
    user = ReadOnlyField(source="user.username")
    game = ReadOnlyField(source="game.title")
    class Meta:
        model = GameSave
        fields = ['id','data','user','game']