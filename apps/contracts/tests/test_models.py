import pytest
from datetime import date, timedelta
from apps.products.models import Product
from apps.ads.models import Ad
from apps.leads.models import Lead
from apps.customers.models import Customer
from apps.contracts.models import Contract


@pytest.mark.django_db
def test_contract_creation():
    product = Product.objects.create(name="Услуга", description="Описание", cost=100)
    ad = Ad.objects.create(name="Кампания", product=product, channel="VK", budget=1000)
    lead = Lead.objects.create(
        first_name="Иван",
        last_name="Иванов",
        phone="+7 999 123 45 67",
        email="ivan@example.com",
        ad=ad
    )
    customer = Customer.objects.create(lead=lead)
    contract = Contract.objects.create(
        name="Тестовый контракт",
        product=product,
        start_date=date.today(),
        end_date=date.today() + timedelta(days=365),
        cost=10000,
        customer=customer
    )
    assert contract.name == "Тестовый контракт"
    assert contract.product.name == "Услуга"
    assert contract.customer.lead.first_name == "Иван"
    assert str(contract) == "Тестовый контракт"
