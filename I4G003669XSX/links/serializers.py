from rest_framework import serializers
# A serializer converts your model(i.e class Link) data to json data format
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    """
    whatever model you want to serialize , state the model_name-followed-by-the_Serializer_keyword.
    THis takes your model as a blueprint which the serializer converts to a json format
"""

    class Meta:
        model = Link
        fields = '__all__'