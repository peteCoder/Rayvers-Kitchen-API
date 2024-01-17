from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        UserModel = get_user_model()

        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                raise serializers.ValidationError(_("No such user found with this email"))
            
            if not user.check_password(password):
                raise serializers.ValidationError(_("Incorrect password"))

            attrs['user'] = user
            attrs['password'] = password
            return attrs
        else:
            raise serializers.ValidationError(_("Must include 'email' and 'password'."))
        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
            "last_login",
            "is_superuser",
        ]


