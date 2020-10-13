from rest_framework import serializers
import models
from django.utils.translation import gettext_lazy as _ 


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    def validate(self, data):
        try:
            user = models.User.objects.filter(username=data.get('username'))
            if(len(user) > 0):
                raise serializers.ValidationError(_("Username already exists"))
        except models.User.DoesNotExist:
            pass

        if not data.get('password') or data.get('confirm_password'):
            raise serializers.ValidationError(_("Empty Password"))

        if data.get('password') != data.get('confirm_password'):
                raise serializers.ValidationError(_("Mismatch"))

    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'password', 'confirm_password', 'is_active')
        extra_kwargs = {'confirm_password': {'read_only': True}}



