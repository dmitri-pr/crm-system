import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from apps.products.models import Product
from apps.ads.models import Ad
from apps.leads.models import Lead
from apps.customers.models import Customer
from apps.contracts.models import Contract
from datetime import date, timedelta


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
def contract(lead):
    return Contract.objects.create(
        name="Тестовый контракт",
        product=Product.objects.create(name="Услуга 2", description="Описание", cost=200),
        start_date=date.today(),
        end_date=date.today() + timedelta(days=365),
        cost=10000,
    )


@pytest.fixture
def customer(lead, contract):
    customer = Customer.objects.create(lead=lead)
    contract.customer = customer
    contract.save()
    return customer


@pytest.mark.django_db
def test_customer_list_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("customers:list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_customer_create_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("customers:create")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_customer_detail_view(client, admin_user, customer):
    client.force_login(admin_user)
    url = reverse("customers:detail", kwargs={"pk": customer.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"].lead.first_name == "Иван"  # noqa


@pytest.mark.django_db
def test_customer_creation(client, admin_user, lead, contract):
    client.force_login(admin_user)
    url = reverse("customers:create")
    data = {
        "lead": lead.pk,
        "contract": contract.pk,
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    assert Customer.objects.count() == 1
    customer = Customer.objects.first()
    assert customer.lead == lead  # noqa
    assert customer.lead.first_name == "Иван"  # noqa


@pytest.mark.django_db
def test_customer_update_view(client, admin_user, customer):
    client.force_login(admin_user)
    url = reverse("customers:update", kwargs={"pk": customer.pk})

    lead = customer.lead  # noqa
    data = {
        "first_name": "Петр",
        "last_name": "Петров",
        "phone": "+7 999 888 77 66",
        "email": "petr@example.com",
        "ad": lead.ad.pk,  # noqa
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200

    lead.refresh_from_db()  # noqa
    assert lead.first_name == "Петр"  # noqa
    assert lead.phone == "+7 999 888 77 66"  # noqa


@pytest.mark.django_db
def test_customer_delete_view(client, admin_user, customer):
    client.force_login(admin_user)
    url = reverse("customers:delete", kwargs={"pk": customer.pk})
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert Customer.objects.count() == 0
