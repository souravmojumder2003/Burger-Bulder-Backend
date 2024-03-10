from rest_framework import serializers
from .models import User, Order, Ingredient,CustomerDetail

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
        'input_type': 'password'
    })


    class Meta:
        model = User
        fields = ['id','email','password']


    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        user = User.objects.create(email, password)
        return user    
    
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ingredient
        fields = '__all__'
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomerDetail
        fields = '__all__'    


class OrderSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerSerializer()
    class Meta:
        model = Order
        fields = '__all__'    

    def create(self, validated_data):
        ingredient = validated_data["ingredients"]
        customer = validated_data["customer"]
        price = validated_data["price"]
        orderTime = validated_data["orderTime"]
        user = validated_data["user"]
        order = Order.objects.create (
            ingredients = IngredientSerializer.create(IngredientSerializer(), ingredient),
            customer= CustomerSerializer.create(CustomerSerializer(),customer),
            orderTime = orderTime,
            price = price,
            user = user
        )

        return order