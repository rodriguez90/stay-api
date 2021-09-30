from django.contrib.auth.models import User
from rest_framework import serializers

from stay.models import Rent, RentImages, RentService
from .service_serialize import ServiceSerializer
from .file_list import FileListSerialize


class RentImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentImages
        fields = '__all__'


class RentServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentService
        fields = '__all__'


class RentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rent
        fields = '__all__'


class RentCreateSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=False)
    images = FileListSerialize()

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        images_data = validated_data.pop('images')

        rent = Rent.objects.create(**validated_data)

        for service_data in services_data:
            rent_service = RentService.objects.create(rent=rent, service_id=service_data.id)

            rent_service.save()

        for image_data in images_data:
            rent_images = RentImages.objects.create(rent=rent, **image_data)

            rent_images.save()

        return rent

    class Meta:
        model = Rent
        fields = ['id', 'name', 'description', 'is_active', 'user',
                  'price', 'phone', 'email', 'adress', 'image', 'images',
                  'created_at', 'updated_at', 'services']
        related_field = ['services', 'user']


