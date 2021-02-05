from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active']
        depth = 1

class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ('__all__')

class MallFloorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MallFloors
        fields = ('__all__')

class VisitorsFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorsFlow
        fields = ('__all__')

class VisitorsFlowAdjustmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorsFlowAdjustments
        fields = ('__all__')

class GrossLeasingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrossLeasingArea
        fields = ('__all__')

class GrossLeasedAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrossLeasedArea
        fields = ('__all__')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('__all__')

class LeasedAreaStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeasedAreaState
        fields = ('__all__')

class StateOfLeasedAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateOfLeasedArea
        fields = ('__all__')

class CommodityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityGroup
        fields = ('__all__')

class LeasedAreaCommodityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeasedAreaCommodityGroup
        fields = ('__all__')

class OrganizationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = ('__all__')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('__all__')

class DivisionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionType
        fields = ('__all__')

class OrganizationDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDivision
        fields = ('__all__')

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('__all__')

class EnterpriseDivisionMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseDivisionMembership
        fields = ('__all__')

class LessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessor
        fields = ('__all__')

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('__all__')

class AccrualTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccrualType
        fields = ('__all__')

class OffsetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffsetType
        fields = ('__all__')

class ContractAccrualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractAccrual
        fields = ('__all__')

class ContractPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractPayment
        fields = ('__all__')

class ContractAccrualOffsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractAccrualOffset
        fields = ('__all__')

class LeasedAreaRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeasedAreaRate
        fields = ('__all__')
