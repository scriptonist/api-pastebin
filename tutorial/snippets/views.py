
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets or create a new snippet_list
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or delete a code snippet_detail
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

   