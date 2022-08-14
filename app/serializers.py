from dataclasses import fields
from rest_framework import serializers
from .models import Competition, Event,EventImage,CompetitionImage, Post, TeamMember

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields= '__all__'

class EventIdImgSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventImage
        fields=['id','img_id']

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Competition
        fields='__all__'

class CompetitionImgSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompetitionImage
        fields=['id','img_id']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamMember
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'