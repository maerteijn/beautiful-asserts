import re

import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from beautiful_asserts.models import Article

## test_article_list ##


@pytest.mark.django_db
def test_article_list__get__assertContains(client):
    article = Article.objects.create(title="My title")

    response = client.get(reverse("article-list"))

    # Check that our newly created article is on the overview page
    assertContains(response, f"<li>{article.title}</li>", html=True)


@pytest.mark.django_db
def test_article_list__get__select(client):
    article = Article.objects.create(title="My title")

    response = client.get(reverse("article-list"))
    assert response.status_code == 200

    article_items = response.select("ul.articles li")

    # Check that our newly created article is on the overview page
    assert len(article_items) == 1
    assert article_items[0].text == article.title


## test_article_create__get ##


@pytest.mark.django_db
def test_article_create__get__assertContains(client):
    response = client.get(reverse("article-create"))

    assertContains(response, "<h1>Create Article</h1>", html=True)
    assertContains(response, '<form method="post">')
    assertContains(
        response,
        '<input type="text" name="title" maxlength="255" required="" id="id_title">',
        html=True,
    )
    assertContains(response, '<input type="submit" name="submit" value="Submit">')


@pytest.mark.django_db
def test_article_create__get__assert_with_regex(client):
    response = client.get(reverse("article-create"))

    assert response.status_code == 200
    assert re.search("<h1.*>Create Article</h1>", str(response.content))
    assert re.search("<form.*>", str(response.content))


@pytest.mark.django_db
def test_article_create__get__select(client):
    response = client.get(reverse("article-create"))

    assert response.status_code == 200

    assert response.select("h1")[0].text == "Create Article"
    assert response.select("form")
    assert response.select("input[name='title']")
    assert response.select("input[type='submit']")


## test_article_create__post_error ##


@pytest.mark.django_db
def test_article_create__post_error__assertContains(client):
    data = dict(title="my title does not start with an uppercase")
    response = client.post(reverse("article-create"), data=data)

    assertContains(response, '<ul class="errorlist">')
    assertContains(
        response, "<li>Should start with an uppercase letter.</li>", html=True
    )


@pytest.mark.django_db
def test_article_create__post_error__select(client):
    data = dict(title="my title does not start with an uppercase")
    response = client.post(reverse("article-create"), data=data)

    assert response.status_code == 200
    assert response.select("ul.errorlist")

    error_messages = response.select("ul.errorlist li")
    assert len(error_messages) == 1
    assert error_messages[0].text == "Should start with an uppercase letter."


## test_article_create__post_success ##


@pytest.mark.django_db
def test_article_create__post_success(client):
    data = dict(title="My correct title")
    response = client.post(reverse("article-create"), data=data)

    assert response.status_code == 302
    assert response.url == reverse("article-list")

    assert Article.objects.filter(**data).exists()
