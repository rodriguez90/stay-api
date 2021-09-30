from rest_framework import serializers
from stay.models import Rent, RentImages, RentService


class FileListSerialize(serializers.Serializer):
    images = serializers.ListField(child=serializers.FilePathField(path='media/uploads/', match='/%Y/%m/%d/'))

    def create(self, validated_data):
        rent = Rent.objects.latest('created_at')
        images = validated_data.pop('images')
        for img in images:
            rent_image = RentImages.objects.create(rent=rent, image=img)
            rent_image.save()
