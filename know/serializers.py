from rest_framework import serializers
from .models import Person, Address, Income, Family,Bank

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    income = IncomeSerializer(many=True)
    family = FamilySerializer(many=True)

    class Meta:
        model = Person
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
