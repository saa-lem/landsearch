from rest_framework import serializers
from .models import Property,Profile



class PropertySerializer(serializers.Serializer)):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    location=serializers.CharField(max_length=20)
    image = serializers.ImageField()


      

    def create(self,validated_data):
        return Property.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)

        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields=['user','image','property','bio','contacts'] 

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.property = validated_data.get('property', instance.property)
        instance.save()
        return instance