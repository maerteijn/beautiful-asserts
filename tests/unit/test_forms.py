import pytest

from beautiful_asserts.forms import ArticleForm
from beautiful_asserts.models import Article


@pytest.mark.django_db
def test_article_form__correct_title():
    title = "My correct title"
    form = ArticleForm(data=dict(title=title))

    assert form.is_valid()
    assert isinstance(form.instance, Article)
    assert form.instance.title == title


@pytest.mark.parametrize(
    "title,expected_error_message",
    (
        ("title not uppercased", "Should start with an uppercase letter."),
        ("My title with a period.", "The period sign is not allowed."),
        (None, "This field is required."),
    ),
)
@pytest.mark.django_db
def test_article_form__invalid_title(title, expected_error_message):
    form = ArticleForm(data=dict(title=title))
    assert not form.is_valid()

    assert "title" in form.errors
    assert form.errors["title"] == [expected_error_message]
