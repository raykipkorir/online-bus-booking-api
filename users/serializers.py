from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class AdminUserSerializer(serializers.ModelSerializer):
    """Serialize AdminUser crud operations"""
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    re_password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phone_number", "password", "re_password"]

    def validate(self, attrs):
        password = attrs["password"]
        re_password = attrs["re_password"]

        if password != re_password:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_superuser(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                phone_number=validated_data['phone_number'],
                password=validated_data["password"]
            )
        return user
