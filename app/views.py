from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event,EventImage,Competition,CompetitionImage, TeamMember,Post
from .serializers import EventSerializer,EventIdImgSerializer,CompetitionSerializer,CompetitionImgSerializer, PostSerializer, TeamMemberSerializer


# Create your views here.

class EventList(APIView):
    def get(self,request):
        event=Event.objects.all()
        serializer=EventSerializer(event,many=True)
        return Response(serializer.data)

class EventImgList(APIView):
    def get(self,request,id):
        img=EventImage.objects.filter(event=id)
        serializer=EventIdImgSerializer(img,many=True)
        return Response(serializer.data)

class CompetitionList(APIView):
    def get(self,request):
        event=Competition.objects.all()
        serializer=CompetitionSerializer(event,many=True)
        return Response(serializer.data)

class CompetitionImgList(APIView):
    def get(self,request,id):
        img=CompetitionImage.objects.filter(event=id)
        serializer=CompetitionImgSerializer(img,many=True)
        return Response(serializer.data)

class TeamMemberList(APIView):
    def get(self,request):
        members=TeamMember.objects.all()
        serializer=TeamMemberSerializer(members,many=True)
        return Response(serializer.data)
class PostList(APIView):
    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)