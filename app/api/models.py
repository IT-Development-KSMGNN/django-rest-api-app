from django.db import models


class Mall(models.Model):

    class Meta:
        verbose_name = "Торговый центр"
        verbose_name_plural = "Торговые центры"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


class MallFloors(models.Model):

    class Meta:
        verbose_name = "Этажи ТЦ"
        verbose_name_plural = "Этажи ТЦ"

    def __str__(self):
        return self.mall.name + " | " + self.name
    
    mall = models.ForeignKey(Mall, on_delete=models.CASCADE, related_name='mall_floor')
    name = models.CharField(blank=True, null=True, max_length=200)
    level = models.IntegerField()
    gross_floor_area = models.FloatField()


class VisitorsFlow(models.Model):

    class Meta:
        verbose_name = "Поток посетителей"
        verbose_name_plural = "Поток посетителей"
        constraints = [
            models.UniqueConstraint(name='mall_date', fields=['mall', 'date'])
            ]

    def __str__(self):
        return self.mall

    mall = models.ForeignKey(Mall, on_delete=models.CASCADE)        
    real_in = models.IntegerField()
    real_out = models.IntegerField()
    date = models.DateField()

class VisitorsFlowAdjustments(models.Model):

    class Meta:
        verbose_name = "Корректировка потока"
        verbose_name_plural = "Корректировки потока"

    def __str__(self):
        return self.mall

    mall = models.ForeignKey(Mall, on_delete=models.CASCADE)
    date = models.DateField()
    real_in = models.IntegerField()
    real_out = models.IntegerField()
    comment = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)


class GrossLeasingArea(models.Model):

    class Meta:
        verbose_name = "Общая площадь аренды"
        verbose_name_plural = "Общие площади аренды"

    def __str__(self):
        pass

    name = models.CharField(blank=False, null=False, max_length=50)
    shopping_mall_floor = models.ForeignKey(MallFloors, on_delete=models.CASCADE)
    area = models.FloatField()
    linked = models.DateField()
    unlinked = models.DateField()
    discription = models.TextField()
    lessor = models.ForeignKey('Lessor', on_delete=models.PROTECT)


class GrossLeasedArea(models.Model):

    class Meta:
        verbose_name = "Общая арендуемая площадь"
        verbose_name_plural = "Общие арендуемые площади"

    def __str__(self):
        pass

    contract = models.ForeignKey('Contract', on_delete=models.PROTECT)
    gross_leasing_area = models.ForeignKey(GrossLeasingArea, on_delete=models.PROTECT)
    date_taken = models.DateField()
    date_return = models.DateField()


class Contract(models.Model):

    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"

    def __str__(self):
        pass

    date = models.DateField()
    number = models.CharField(blank=False, null=False, max_length=100)
    lessor = models.ForeignKey('Lessor', on_delete=models.PROTECT)
    tenant = models.ForeignKey('Tenant', on_delete=models.PROTECT)


class LeasedAreaState(models.Model):

    class Meta:
        verbose_name = "Состояние арендуемой зоны"
        verbose_name_plural = "Состояния арендуемых зон"

    def __str__(self):
        pass

    date = models.DateField()
    state = models.ForeignKey('StateOfLeasedArea', on_delete=models.PROTECT)
    gross_leased_area = models.ForeignKey(GrossLeasedArea, on_delete=models.PROTECT)


class StateOfLeasedArea(models.Model):

    class Meta:
        verbose_name = "Тип состояния арендуемой зоны"
        verbose_name_plural = "Типы состояний арендуемых зон"

    def __str__(self):
        pass
    
    name = models.CharField(blank=False, null=False, max_length=150)
    discription = models.TextField(blank=True, null=True)


class CommodityGroup(models.Model):

    class Meta:
        verbose_name = "Товарная группа"
        verbose_name_plural = "Товарные группы"

    def __str__(self):
        pass
    
    name = models.CharField(blank=False, null=False, max_length=50)


class LeasedAreaCommodityGroup(models.Model):

    class Meta:
        verbose_name = "Товарная группа арендуемой зоны"
        verbose_name_plural = "Товарные группы арендуемых зон"

    def __str__(self):
        pass
    
    gross_leased_area = models.ForeignKey(GrossLeasedArea, on_delete=models.PROTECT)
    date_from = models.DateField()
    date_till = models.DateField()
    commodity_group = models.ForeignKey(CommodityGroup, on_delete=models.PROTECT)

class OrganizationType(models.Model):

    class Meta:
        verbose_name = "Тип организации"
        verbose_name_plural = "Типы организаций"

    def __str__(self):
        pass

    short_name = models.CharField(blank=False, null=False, max_length=250)
    full_name = models.CharField(blank=False, null=False, max_length=350)

class Organization(models.Model):

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        pass
    
    short_name = models.CharField(blank=False, null=False, max_length=250)
    full_name = models.CharField(blank=False, null=False, max_length=350)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.PROTECT)
    inn = models.CharField(blank=True, null=True, max_length=50)    
    

class DivisionType(models.Model):

    class Meta:
        verbose_name = "Тип подразделения"
        verbose_name_plural = "Типы подразделений"

    def __str__(self):
        pass

    name = models.CharField(blank=False, null=False, max_length=150)
    discription = models.TextField(blank=True, null=True)

class OrganizationDivision(models.Model):
    
    class Meta:
        verbose_name = "Подразделение организации"
        verbose_name_plural = "Подразделения организаций"

    def __str__(self):
        pass
            
    name = models.CharField(blank=False, null=False, max_length=150)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    kpp = models.CharField(blank=True, null=True, max_length=80)
    division_type = models.ForeignKey(DivisionType, on_delete=models.PROTECT)

class Enterprise(models.Model):

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"

    def __str__(self):
        pass
    
    name = models.CharField(blank=False, null=False, max_length=150)
    discription = models.TextField(blank=True, null=True)

class EnterpriseDivisionMembership(models.Model):
    
    class Meta:
        verbose_name = "Членство в корпоративном подразделении"
        verbose_name_plural = "Членства в корпоративных подразделениях"

    def __str__(self):
        pass
    
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)
    organization_division = models.ForeignKey(OrganizationDivision, on_delete=models.PROTECT)
    discription = models.TextField(blank=True, null=True)   

class Lessor(models.Model):

    class Meta:
        verbose_name = "Арендодатель"
        verbose_name_plural = "Арендодатели"

    def __str__(self):
        pass

    organization_division = models.ForeignKey(OrganizationDivision, on_delete=models.PROTECT, null=True)
    
class Tenant(models.Model):

    class Meta:
        verbose_name = "Арендатор"
        verbose_name_plural = "Арендаторы"

    def __str__(self):
        pass
    
    organization_division = models.ForeignKey(OrganizationDivision, on_delete=models.PROTECT, null=True)

class AccrualType(models.Model):

    class Meta:
        verbose_name = "Тип начисления"
        verbose_name_plural = "Типы начислений"

    def __str__(self):
        pass
    
    name = models.CharField(blank=False, null=False, max_length=150)
    discription = models.TextField(blank=True, null=True)

class OffsetType(models.Model):

    class Meta:
        verbose_name = "Тип корректировки счёта"
        verbose_name_plural = "Типы корректировок счетов"

    def __str__(self):
        pass
    
    name = models.CharField(blank=False, null=False, max_length=150)
    discription = models.TextField(blank=True, null=True)

class ContractAccrual(models.Model):

    class Meta:
        verbose_name = "Начисление по договору"
        verbose_name_plural = "Начисления по договорам"

    def __str__(self):
        pass
    
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.FloatField()
    accrual_type = models.ForeignKey(AccrualType, on_delete=models.PROTECT)
    operation_date_1c = models.DateField()
    payment_deadline = models.DateField()

class ContractPayment(models.Model):

    class Meta:
        verbose_name = "Оплата по договору"
        verbose_name_plural = "Оплаты по договорам"

    def __str__(self):
        pass

    operation_guid_1c = models.CharField(blank=True, null=True, max_length=300)
    date = models.DateField()
    amount = models.FloatField()
    bank_inn = models.CharField(blank=True, null=True, max_length=150)
    bank_bic = models.CharField(blank=True, null=True, max_length=150)
    bank_account_number = models.CharField(blank=True, null=True, max_length=250)
    organization_inn = models.CharField(blank=True, null=True, max_length=150)
    organization_kpp = models.CharField(blank=True, null=True, max_length=150)

class ContractAccrualOffset(models.Model):

    class Meta:
        verbose_name = "Корректировка начсления по договору"
        verbose_name_plural = "Корректировки начислений по договорам"

    def __str__(self):
        pass
    
    date = models.DateField()
    amount = models.FloatField()
    offset_type = models.ForeignKey(OffsetType, on_delete=models.PROTECT)
    contract_accrual = models.ForeignKey(ContractAccrual, on_delete=models.PROTECT)
    operation_date_1c = models.DateField()
    contract_payment = models.ForeignKey(ContractPayment, on_delete=models.PROTECT, null=True)
    contract_accrual_followref = models.ForeignKey(ContractAccrual, on_delete=models.PROTECT, null=True, related_name='followref')

class LeasedAreaRate(models.Model):

    class Meta:
        verbose_name = "Арендованная площадь"
        verbose_name_plural = "Арендованные площади"

    def __str__(self):
        pass

    date = models.DateField()
    rate_fee_per_square_meter_per_day = models.FloatField()
    gross_leased_area = models.ForeignKey(GrossLeasedArea, on_delete=models.PROTECT)
    rate_as_contract = models.FloatField()
    rate_period = models.CharField(blank=True, null=True, max_length=150)

    