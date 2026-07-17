import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from apps.products.models import Product


@pytest.fixture
def admin_user():
    return User.objects.create_superuser(username="admin", password="admin")


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def product():
    return Product.objects.create(
        name="Услуга",
        description="Описание",
        cost=100
    )


@pytest.mark.django_db
def test_product_create_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("products:create")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_creation(client, admin_user):
    client.force_login(admin_user)
    url = reverse("products:create")
    data = {
        "name": "Новый продукт",
        "description": "Описание",
        "cost": 100.00,
    }
    response = client.post(url, data, follow=True)

    assert Product.objects.count() == 1
    assert Product.objects.first().name == "Новый продукт"

    assert response.status_code == 200
    assert response.redirect_chain[0][0] == reverse("products:list")


@pytest.mark.django_db
def test_product_detail_view(client, admin_user, product):
    client.force_login(admin_user)
    url = reverse("products:detail", kwargs={"pk": product.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"].name == "Услуга"


@pytest.mark.django_db
def test_product_list_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("products:list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_list_contains_multiple_products(client, admin_user):
    client.force_login(admin_user)

    Product.objects.create(name='Услуга 1', description='Описание', cost=100)
    Product.objects.create(name='Услуга 2', description='Описание', cost=200)

    url = reverse('products:list')
    response = client.get(url)

    assert response.status_code == 200
    assert "Услуга 1" in response.content.decode()
    assert "Услуга 2" in response.content.decode()
