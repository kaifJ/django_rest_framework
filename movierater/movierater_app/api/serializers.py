from rest_framework import serializers
from movierater_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']
        # read_only_fields = ['name', 'description']

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                "Name and Description should be different"
            )
        return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "Name is too short"
            )
        return value


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     description = serializers.CharField(max_length=200)
#     active = serializers.BooleanField(default=True)

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description
#         )
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "Name and Description should be different"
#             )
#         return data
