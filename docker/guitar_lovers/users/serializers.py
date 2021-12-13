from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        if data.get('first_name') == '':
            raise serializers.ValidationError('First name cannot be empty')

        if data.get('last_name') == '':
            raise serializers.ValidationError('Last name cannot be empty')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'bio', 'country', 'city', 'guitar']
