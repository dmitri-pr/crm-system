import pytest
from apps.products.models import Product
from apps.ads.models import Ad


@pytest.mark.django_db
def test_ad_creation():
    product = Product.objects.create(name="Услуга", description="Описание", cost=100)
    ad = Ad.objects.create(
        name="Тестовая кампания",
        product=product,
        channel="VK",
        budget=1000
    )
    assert ad.name == "Тестовая кампания"
    assert str(ad) == "Тестовая кампания"
