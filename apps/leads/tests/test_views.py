import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from apps.products.models import Product
from apps.ads.models import Ad
from apps.leads.models import Lead


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
def test_lead_list_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("leads:list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_lead_create_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("leads:create")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_lead_detail_view(client, admin_user, lead):
    client.force_login(admin_user)
    url = reverse("leads:detail", kwargs={"pk": lead.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"].first_name == "Иван"


@pytest.mark.django_db
def test_lead_creation(client, admin_user, ad):
    client.force_login(admin_user)
    url = reverse("leads:create")
    data = {
        "first_name": "Петр",
        "last_name": "Петров",
        "phone": "+7 999 888 77 66",
        "email": "petr@example.com",
        "ad": ad.pk,
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    assert Lead.objects.count() == 1
    assert Lead.objects.first().first_name == "Петр"


@pytest.mark.django_db
def test_lead_update_view(client, admin_user, lead):
    client.force_login(admin_user)
    url = reverse("leads:update", kwargs={"pk": lead.pk})
    data = {
        "first_name": "Иван",
        "last_name": "Иванов",
        "phone": "+7 999 111 22 33",
        "email": "ivan_new@example.com",
        "ad": lead.ad.pk,  # noqa
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    lead.refresh_from_db()
    assert lead.phone == "+7 999 111 22 33"
    assert lead.email == "ivan_new@example.com"


@pytest.mark.django_db
def test_lead_delete_view(client, admin_user, lead):
    client.force_login(admin_user)
    url = reverse("leads:delete", kwargs={"pk": lead.pk})
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert Lead.objects.count() == 0


@pytest.mark.django_db
def test_lead_ad_relation(client, admin_user, lead, ad):
    client.force_login(admin_user)
    url = reverse("ads:detail", kwargs={"pk": ad.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert lead.ad == ad
