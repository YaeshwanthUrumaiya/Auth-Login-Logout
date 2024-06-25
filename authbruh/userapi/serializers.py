from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

usermodel = get_user_model()

class userregisterserializer(serializers.ModelSerializer):
    class Meta:
        model = usermodel
        fields = '__all__'
    def create(self, clean_data):
        user_obj = usermodel.objects.create_user(email = clean_data['email'], password = clean_data['password'])
        user_obj['username'] = clean_data['username']
        user_obj.save()
        return user_obj
        
class userloginserializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    pword = serializers.CharField()
    def check_user(self, clean_data):
        user = authenticate(username = clean_data['email'], password = clean_data['password'])
        if not user: 
            raise ValueError('user not there')
        return user
        
class userserializer(serializers.ModelSerializer):
    class Meta:
        model = usermodel
        fields = ('email', 'username')