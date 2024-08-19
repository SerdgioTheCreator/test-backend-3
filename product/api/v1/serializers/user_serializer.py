from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    def create(self, validated_data):
        """Создание новой подписки."""
        return Subscription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Обновление существующей подписки."""
        instance.user = validated_data.get('user', instance.user)
        instance.course = validated_data.get('course', instance.course)
        instance.save()
        return instance

    # TODO

    class Meta:
        model = Subscription
        fields = (
            'user',
            'course'
            # TODO
        )
