from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from blog.serializer import PostSerializer, CommentSerializer
from blog.models import Post, Comment

class GenericPostView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixins):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class GenericCommentView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixins):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
