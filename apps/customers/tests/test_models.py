import pytest
from apps.products.models import Product
from apps.ads.models import Ad
from apps.leads.models import Lead
from apps.customers.models import Customer


@pytest.mark.django_db
def test_customer_creation():
    product = Product.objects.create(name="Услуга", description="Описание", cost=100)
    ad = Ad.objects.create(name="Кампания", product=product, channel="Facebook", budget=1000)
    lead = Lead.objects.create(
        first_name="Иван",
        last_name="Иванов",
        phone="+7 999 123 45 67",
        email="ivan@example.com",
        ad=ad
    )
    customer = Customer.objects.create(lead=lead)
    assert str(customer) == "Иванов Иван"
    assert customer.lead == lead
