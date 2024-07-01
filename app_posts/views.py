from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# local
from . import models
from . import serializers


# posts
class ListPosts(APIView):
    def get(self, request):
        posts = models.Posts.objects.all()
        serializer = serializers.PostSerializers(posts, many=True)
        serializer_data = {
            'posts': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class PostDeatil(APIView):
    def get(self, request, pk):
        try:
            posts = models.Posts.objects.get(pk=pk)
            serializer = serializers.PostSerializers(posts)
            serializer_data = {
                'posts': serializer.data,
                'status': 'SUCCESS',
                'status_code': status.HTTP_200_OK
            }
        except Exception as exp:
            serializer_data = {
                'ERROR': 'We can`t find it',
                'status': 'NOT FOUND',
                'status_code': status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)


class PostsCreate(APIView):
    def post(self, request):
        serializer = serializers.PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'post': serializer.data,
                    'status': 'SUCCESS',
                    'status_code': status.HTTP_201_CREATED
                }
            )
        else:
            return Response(
                {
                    'ERROR': 'We couldn`t create your post',
                    'status': 'ERROR',
                    'status_code': status.HTTP_400_BAD_REQUEST
                }
            )


class PutPost(APIView):
    def put(self, request, pk):
        serializer_data = {}
        try:
            posts = models.Posts.objects.get(pk=pk)
            serializer = serializers.PostSerializers(posts, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    'post': serializer.data,
                    'status': 'SUCSESS',
                    'status_code': status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    'ERROR': str(serializer.errors),
                    'status': 'ERROR',
                    'status_code': status.HTTP_400_BAD_REQUEST
                }
        except Exception as exp:
            serializer_data = {
                'ERROR': 'Can`t find post to update',
                'status': 'ERROR',
                'status_code': status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)


class PostsDelete(APIView):
    def delete(self, request, pk):
        try:
            posts = models.Posts.objects.get(pk=pk)
            posts.delete()
            serializer_data = {
                'posts': f"post has been deleted successfully!",
                'status': 'SUCSESS',
                'status_code': status.HTTP_200_OK
            }
        except Exception as exp:
            serializer_data = {
                'ERROR': str(exp),
                'status': 'ERROR',
                'status_code': status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)


# comments
class ListComments(APIView):
    def get(self, request, pk):
        comments = models.Comments.objects.filter(post=pk)
        serializer = serializers.CommentSerializer(comments, many=True)
        serializer_data = {
            'comments': serializer.data,
            'status': 'SUCCESS',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class CreateComment(APIView):
    def post(self, request, pk):
        try:
            post = models.Posts.objects.get(pk=pk)  # Get the post with the given ID
        except Exception as exp:
            return Response(
                {
                    'ERROR': str(exp),
                    'status': 'ERROR',
                    'status_code': status.HTTP_404_NOT_FOUND
                }
            )

        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)  # Associate the comment with the post
            return Response(
                {
                    'comment': serializer.data,
                    'status': 'SUCCESS',
                    'status_code': status.HTTP_201_CREATED
                }
            )
        else:
            return Response(
                {
                    'ERROR': 'We couldn\'t create your comment',
                    'status': 'ERROR',
                    'status_code': status.HTTP_400_BAD_REQUEST
                }
            )


class PutComment(APIView):
    def put(self, request, pk):
        serializer_data = {}
        try:
            comment = models.Comments.objects.get(pk=pk)
            serializer = serializers.PostSerializers(comment, data=request.data)
            if serializer.is_valid():
                print(serializer.data)
                serializer.save()
                serializer_data = {
                    'comment': serializer.data,
                    'status': 'SUCCESS',
                    'status_code': status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    'ERROR': str(serializer.errors),
                    'status': 'ERROR',
                    'status_code': status.HTTP_400_BAD_REQUEST
                }
        except Exception as exp:
            serializer_data = {
                'ERROR': str(exp),
                'status': 'ERROR',
                'status_code': status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)
