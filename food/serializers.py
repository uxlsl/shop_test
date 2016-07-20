# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('name', 'category')

    def update(self, instance, validated_data):
        import traceback;
        traceback.print_stack()
        print(instance)
        print(validated_data)
        return super(GoodsSerializer, self).update(instance, validated_data)
