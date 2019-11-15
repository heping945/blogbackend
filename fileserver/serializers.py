from rest_framework import serializers

from .models import PostImg
from .utils import getFileMd5, getFileSize, judgeFileType, rename


class PostImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImg
        fields = '__all__'
        read_only_fields = ('imgMd5', 'name')

    def validate(self, attrs):
        img = attrs['img']
        md5 = getFileMd5(img)
        name = rename(img.name)
        # 判断图片大小
        file_size = getFileSize(img.size)
        if not file_size:
            raise serializers.ValidationError('图片太大')
        attrs['imgMd5'] = md5
        attrs['name'] = name
        return attrs

    def create(self, validated_data):
        img = validated_data['img']
        print(self.context,'self.context')
        print(self.context['request'].user,'self.context.user')
        # 判断图片是否存在
        md5 = getFileMd5(img)
        imgobj = PostImg.objects.filter(imgMd5=md5)
        if imgobj:
            return PostImg.objects.filter(imgMd5=md5).first()
        return PostImg.objects.create(**validated_data)