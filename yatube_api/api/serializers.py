from rest_framework.serializers import (CurrentUserDefault,
                                        ValidationError,
                                        ModelSerializer,
                                        SlugRelatedField,
                                        UniqueTogetherValidator)

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', queryset=User.objects.all(),
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Вы уже подписаны на данного автора!'
            )
        ]

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise ValidationError(
                'Нельзя подписаться самому на себя!'
            )
        return value
