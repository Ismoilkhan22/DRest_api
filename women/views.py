from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response

from women.models import Women
from women.serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    serializer_class = WomenSerializer
    def get(self, request):
        lst = Women.objects.all().values()

        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            contents=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})


