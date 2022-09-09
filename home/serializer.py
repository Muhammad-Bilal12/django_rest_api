from rest_framework import serializers
from .models import Todo
import re

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def validate(self, validated_data):
        if validated_data.get('todo_title'):    
            todo_title = validated_data['todo_title']
            regex = re.compile("[@_!#$%^&*()<>?/|}{~:]")

            if len(todo_title)<3:
                raise serializers.ValidationError('todo title should be mode than 3')

            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('todo title cannot contain special characters')

        return validated_data
