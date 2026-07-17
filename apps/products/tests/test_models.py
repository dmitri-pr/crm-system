import pytest
from apps.products.models import Product


@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name="Тестовая услуга",
        description="Описание",
        cost=100.00
    )
    assert product.name == "Тестовая услуга"
    assert str(product) == "Тестовая услуга"
