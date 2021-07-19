from quotes.models import Quote
from rest_framework import serializers


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ['_id', 'quote', 'author']
