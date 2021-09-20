from django.shortcuts import render
from .models import Reply
from .serializers import ReplySerializer
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ReplyList(APIView):
  
  def get(self, request): 
      reply = Reply.objects.all()
      serializer = ReplySerializer(reply, many=True)
      return Response(serializer.data)

  def post(self, request):
    serializer = ReplySerializer(data=request.data)
    if serializer.is_vaild():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class ReplyDetail(APIView): 

    def get_reply(self, pk):
      try:
        return Reply.objects.get(pk=pk)
      except Reply.DoesNotExist:  
        raise

    def get(self,request,pk):
      song = self.get_reply(pk)
      serializers = ReplySerializer(song)
      return Response(serializers.data)

    def put(self,request,pk):
      reply = self.get_comment(pk)
      serializer = ReplySerializer(reply, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete (self,request,pk):
      reply = self.get_reply(pk)
      reply.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)        
     