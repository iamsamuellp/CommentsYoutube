from django.shortcuts import render
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404





class CommentList(APIView):

  def get(self, request):
    comment =Comments.objects.all()
    serializer = CommentsSerializer(comment, many=True)
    return Response(serializer.data)

  def post(self, request): 
      serializer = CommentsSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
      
class CommentDetail(APIView): 

    def get_comment(self, pk):
      try:
        return Comments.objects.get(pk=pk)
      except Comments.DoesNotExist:  
        raise

    def get(self,request,pk):
      song = self.get_comment(pk)
      serializers = CommentsSerializer(song)
      return Response(serializers.data)

    def put(self,request,pk):
      comments = self.get_comment(pk)
      serializer = CommentsSerializer(comments, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete (self,request,pk):
      comments = self.get_comment(pk)
      comments.delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 
         