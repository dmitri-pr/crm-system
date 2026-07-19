import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from apps.products.models import Product
from apps.ads.models import Ad


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
        name="Тестовая кампания",
        product=product,
        channel="VK",
        budget=1000
    )


@pytest.mark.django_db
def test_ad_list_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("ads:list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ad_create_view(client, admin_user):
    client.force_login(admin_user)
    url = reverse("ads:create")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ad_detail_view(client, admin_user, ad):
    client.force_login(admin_user)
    url = reverse("ads:detail", kwargs={"pk": ad.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"].name == "Тестовая кампания"


@pytest.mark.django_db
def test_ad_creation(client, admin_user, product):
    client.force_login(admin_user)
    url = reverse("ads:create")
    data = {
        "name": "Новая кампания",
        "product": product.pk,
        "channel": "Google",
        "budget": 5000,
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    assert Ad.objects.count() == 1
    ad = Ad.objects.first()
    assert ad.name == "Новая кампания"  # noqa
    assert ad.budget == 5000  # noqa


@pytest.mark.django_db
def test_ad_update_view(client, admin_user, ad, product):
    client.force_login(admin_user)
    url = reverse("ads:update", kwargs={"pk": ad.pk})
    data = {
        "name": "Обновлённая кампания",
        "product": product.pk,
        "channel": "Yandex",
        "budget": 7000,
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    ad.refresh_from_db()
    assert ad.name == "Обновлённая кампания"
    assert ad.channel == "Yandex"
    assert ad.budget == 7000


@pytest.mark.django_db
def test_ad_delete_view(client, admin_user, ad):
    client.force_login(admin_user)
    url = reverse("ads:delete", kwargs={"pk": ad.pk})
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert Ad.objects.count() == 0


@pytest.mark.django_db
def test_ad_product_relation(client, admin_user, ad, product):
    client.force_login(admin_user)
    url = reverse("ads:detail", kwargs={"pk": ad.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"].product == product
    assert response.context["object"].product.name == "Услуга"
