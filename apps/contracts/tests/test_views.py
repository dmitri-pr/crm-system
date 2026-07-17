import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta

from apps.products.models import Product
from apps.ads.models import Ad
from apps.leads.models import Lead
from apps.customers.models import Customer
from apps.contracts.models import Contract


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


@pytest.fixture
def product2():
    return Product.objects.create(
        name="Услуга 2",
        description="Описание",
        cost=200
    )


@pytest.fixture
def ad(product):
    return Ad.objects.create(
        name="Кампания",
        product=product,
        channel="Facebook",
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


@pytest.fixture
def customer(lead):
    return Customer.objects.create(lead=lead)


@pytest.fixture
def contract(customer, product):
    return Contract.objects.create(
        name="Тестовый контракт",
        product=product,
        start_date=date.today(),
        end_date=date.today() + timedelta(days=365),
        cost=10000,
        customer=customer
    )


@pytest.mark.django_db
def test_contract_list_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("contracts:list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_contract_create_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("contracts:create")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_contract_detail_view(client, admin_user, contract):
    client.force_login(admin_user)
    url = reverse("contracts:detail", kwargs={"pk": contract.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"].name == "Тестовый контракт"


@pytest.mark.django_db
def test_contract_delete_view(client, admin_user, contract):
    client.force_login(admin_user)
    url = reverse("contracts:delete", kwargs={"pk": contract.pk})
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert Contract.objects.count() == 0


@pytest.mark.django_db
def test_contract_customer_relation(client, admin_user, contract, customer):
    client.force_login(admin_user)
    url = reverse("contracts:detail", kwargs={"pk": contract.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"].customer == customer
    assert response.context["object"].customer.lead.first_name == "Иван" # noqa
