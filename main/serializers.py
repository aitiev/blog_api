from rest_framework import serializers

from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']


class PostSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # author = serializers.EmailField(source='author.email')
    # '26-01-2020 15:45:34'
    # input_formats = ['%d-%m-%Y %H:%M:%S'] can be used for input of date time
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'category', 'created_at', 'image']

    def __get_image_url(self, instance):
        request = self.context.get('request')
        if instance.image:
            url = instance.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        post = Post.objects.create(**validated_data)
        return post

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self.__get_image_url(instance)
        representation['category'] = CategorySerializer(instance.category).data
        representation['author'] = instance.author.email
        return representation
