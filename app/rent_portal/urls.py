from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api.views import *
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


router = routers.DefaultRouter()
router.register(r'malls', MallViewSet)
router.register(r'floormalls', MallFloorsViewSet)
router.register(r'visitors_flow', VisitorsFlowViewSet)
router.register(r'visitors_flow_adjustments', VisitorsFlowAdjustmentsViewSet)
router.register(r'gross_leasing_area', GrossLeasingAreaViewSet)
router.register(r'gross_leased_area', GrossLeasedAreaViewSet)
router.register(r'contract', ContractViewSet)
router.register(r'leased_area_state', LeasedAreaStateViewSet)
router.register(r'state_of_leased_area', StateOfLeasedAreaViewSet)
router.register(r'commodity_group', CommodityGroupViewSet)
router.register(r'leased_area_commodity_group', LeasedAreaCommodityGroupViewSet)
router.register(r'organization_type', OrganizationTypeViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'division_type', DivisionTypeViewSet)
router.register(r'organization_division', OrganizationDivisionViewSet)
router.register(r'enterprise', EnterpriseViewSet)
router.register(r'enterprise_division_membership', EnterpriseDivisionMembershipViewSet)
router.register(r'lessor', LessorViewSet)
router.register(r'tenant', TenantViewSet)
router.register(r'accrual_type', AccrualTypeViewSet)
router.register(r'offset_type', OffsetTypeViewSet)
router.register(r'contract_accrual', ContractAccrualViewSet)
router.register(r'contract_payment', ContractPaymentViewSet)
router.register(r'contract_accrual_offset', ContractAccrualOffsetViewSet)
router.register(r'leased_area_rate', LeasedAreaRateViewSet)


urlpatterns = [
	path('api-token-auth/', obtain_jwt_token),
	path('api-token-verify/', verify_jwt_token),
	path('api-token-refresh/', refresh_jwt_token),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include((router.urls, 'api'))),
]

