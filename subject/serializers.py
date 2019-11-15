from rest_framework import serializers

from .models import Topic,Chapter
from .utils import getFileMd5, judgeFileType, rename



class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('url','id','title','desc','urltag','reproduce','reproduce_source','get_first_id','codestyle','ifshow')
        extra_kwargs = {
            'url': {'view_name': 'topic-detail','lookup_field':'urltag'},
        }

class TopicSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id','title','urltag','codestyle')


class ChapterSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())
    class Meta:
        model = Chapter
        fields = '__all__'
        read_only_fields = ('md5', 'title','md_body')


    def validate(self, attrs):
        mdfile = attrs['md_File']
        md5 = getFileMd5(mdfile)
        name  = mdfile.name
        filetype = judgeFileType(name)
        title = name[:-3]
        # 判断文件类型
        if not filetype:
            raise  serializers.ValidationError("不是有效的md格式文件")

        # 读取文件转化成str
        for chunk in mdfile.chunks():
            mdbody=str(chunk,'utf-8')

        attrs['md5'] = md5
        attrs['md_body'] = mdbody
        attrs['title'] = title
        return attrs

    def create(self, validated_data):
        mdfile = validated_data['md_File']
        # 判断文件是否存在
        md5 = getFileMd5(mdfile)
        mdobj = Chapter.objects.filter(md5=md5)
        if mdobj:
            return Chapter.objects.filter(md5=md5).first()
        # topic = validated_data.pop('topic')
        # print(topic)
        # topic = Topic.objects.update_or_create(**topic)
        # chapter=Chapter.objects.create(topic=topic, **validated_data)
        return Chapter.objects.create(**validated_data)


class ChapterSimpleSerializer(serializers.ModelSerializer):
    topic = TopicSimpleSerializer()


    class Meta:
        model = Chapter
        fields = ('id','title','topic','order')

class ChapterDetailSerializer(serializers.ModelSerializer):
    topic = TopicSimpleSerializer()

    class Meta:
        model = Chapter
        fields = ('id','title','topic','md5','md_body','create_date','order')

