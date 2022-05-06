from django.db.models import OuterRef
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from sub.models import Base, SubModel
from sub.serializers import SubModelSerializer


class Views(ModelViewSet):
    queryset = Base.objects.all()
    serializer_class = SubModelSerializer

    def get_queryset(self):
        qs = Base.objects.all()
        qs = qs.annotate(last=SubModel.objects.filter(base_ptr=OuterRef("pk")).values_list("last")[:1])
        return qs