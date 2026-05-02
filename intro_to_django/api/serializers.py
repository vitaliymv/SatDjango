from rest_framework import serializers

class CustomTaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    is_completed = serializers.BooleanField(default=False)

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title is too short")

        if "bad" in value.lower():
            raise serializers.ValidationError("Title is bad")

        return value

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description are equal")

        return data

from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title is too short")

        if "bad" in value.lower():
            raise serializers.ValidationError("Title is bad")

        return value