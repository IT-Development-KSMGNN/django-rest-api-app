from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class MallViewSet(viewsets.ModelViewSet):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer

class MallFloorsViewSet(viewsets.ModelViewSet):
    queryset = MallFloors.objects.all()
    serializer_class = MallFloorsSerializer

class VisitorsFlowViewSet(viewsets.ModelViewSet):
    queryset = VisitorsFlow.objects.all()
    serializer_class = VisitorsFlowSerializer

class VisitorsFlowAdjustmentsViewSet(viewsets.ModelViewSet):
    queryset = VisitorsFlowAdjustments.objects.all()
    serializer_class = VisitorsFlowAdjustmentsSerializer

class GrossLeasingAreaViewSet(viewsets.ModelViewSet):
    queryset = GrossLeasingArea.objects.all()
    serializer_class = GrossLeasingAreaSerializer

class GrossLeasedAreaViewSet(viewsets.ModelViewSet):
    queryset = GrossLeasedArea.objects.all()
    serializer_class = GrossLeasedAreaSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class LeasedAreaStateViewSet(viewsets.ModelViewSet):
    queryset = LeasedAreaState.objects.all()
    serializer_class = LeasedAreaStateSerializer

class StateOfLeasedAreaViewSet(viewsets.ModelViewSet):
    queryset = StateOfLeasedArea.objects.all()
    serializer_class = StateOfLeasedAreaSerializer

class CommodityGroupViewSet(viewsets.ModelViewSet):
    queryset = CommodityGroup.objects.all()
    serializer_class = CommodityGroupSerializer

class LeasedAreaCommodityGroupViewSet(viewsets.ModelViewSet):
    queryset = LeasedAreaCommodityGroup.objects.all()
    serializer_class = LeasedAreaCommodityGroupSerializer

class OrganizationTypeViewSet(viewsets.ModelViewSet):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class DivisionTypeViewSet(viewsets.ModelViewSet):
    queryset = DivisionType.objects.all()
    serializer_class = DivisionTypeSerializer

class OrganizationDivisionViewSet(viewsets.ModelViewSet):
    queryset = OrganizationDivision.objects.all()
    serializer_class = OrganizationDivisionSerializer

class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class EnterpriseDivisionMembershipViewSet(viewsets.ModelViewSet):
    queryset = EnterpriseDivisionMembership.objects.all()
    serializer_class = EnterpriseDivisionMembershipSerializer

class LessorViewSet(viewsets.ModelViewSet):
    queryset = Lessor.objects.all()
    serializer_class = LessorSerializer

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class AccrualTypeViewSet(viewsets.ModelViewSet):
    queryset = AccrualType.objects.all()
    serializer_class = AccrualTypeSerializer

class OffsetTypeViewSet(viewsets.ModelViewSet):
    queryset = OffsetType.objects.all()
    serializer_class = OffsetTypeSerializer

class ContractAccrualViewSet(viewsets.ModelViewSet):
    queryset = ContractAccrual.objects.all()
    serializer_class = ContractAccrualSerializer

class ContractPaymentViewSet(viewsets.ModelViewSet):
    queryset = ContractPayment.objects.all()
    serializer_class = ContractPaymentSerializer

class ContractAccrualOffsetViewSet(viewsets.ModelViewSet):
    queryset = ContractAccrualOffset.objects.all()
    serializer_class = ContractAccrualOffsetSerializer

class LeasedAreaRateViewSet(viewsets.ModelViewSet):
    queryset = LeasedAreaRate.objects.all()
    serializer_class =LeasedAreaRateSerializer
