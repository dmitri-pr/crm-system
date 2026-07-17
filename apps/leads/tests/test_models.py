import pytest
from apps.products.models import Product
from apps.ads.models import Ad
from apps.leads.models import Lead


@pytest.fixture
def product():
    return Product.objects.create(
        name="Услуга",
        description="Описание",
        cost=100
    )


@pytest.fixture
def ad(product):
    return Ad.objects.create(
        name="Кампания",
        product=product,
        channel="VK",
        budget=1000
    )


@pytest.fixture
def lead(ad):
    return Lead.objects.create(
        first_name="Иван",
        last_name="Иванов",
        phone="+7 999 123 45 67",
        email="ivan@example.com",
        ad=ad
    )


@pytest.mark.django_db
def test_lead_str(lead):
    assert str(lead) == "Иванов Иван"


@pytest.mark.django_db
def test_lead_ad_relation(lead, ad):
    assert lead.ad == ad
    assert lead.ad.name == "Кампания"
    assert lead.ad.budget == 1000


@pytest.mark.django_db
def test_lead_reverse_relation(lead, ad):
    assert ad.leads.count() == 1
    assert ad.leads.first() == lead
