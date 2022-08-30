from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModalSerializer):
    class Meta:
    	fields = ['id','title','author']
    	
    		