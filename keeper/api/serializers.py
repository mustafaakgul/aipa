from rest_framework.serializers import ModelSerializer

from keeper.models import Keeper, Project, User


class KeeperListSerializer(ModelSerializer):
    class Meta:
        model = Keeper
        fields = ('id', 'name', 'description', 'size', 'status', 'assignee', 'target_date')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['targetDate'] = representation.pop('target_date')
        return representation  
    

class KeeperCreateSerializer(ModelSerializer):
    class Meta:
        model = Keeper
        fields = ('name', 'description', 'size', 'assignee', 'target_date')

    def to_internal_value(self, data):
        if 'targetDate' in data:
            data['target_date'] = data.pop('targetDate')
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['targetDate'] = representation.pop('target_date')
        return representation  
    

class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name', 'description')


class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description')


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
