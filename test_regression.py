import pytest
import requests


@pytest.mark.regression
def test_mavjud_bolmagan_post_404_qaytaradi(base_url):
    javob = requests.get(f"{base_url}/posts/99999")
    assert javob.status_code == 404


@pytest.mark.regression
def test_yangi_post_yaratish(base_url, yangi_post_data):
    javob = requests.post(f"{base_url}/posts", json=yangi_post_data)
    assert javob.status_code == 201
    assert javob.json()["title"] == "Test post"


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_post_id_boyicha_mavjud(base_url, post_id):
    javob = requests.get(f"{base_url}/posts/{post_id}")
    assert javob.status_code == 200
    assert javob.json()["id"] == post_id


# Bu test HAM regression, HAM slow
@pytest.mark.regression
@pytest.mark.slow
def test_barcha_postlar_soni(base_url):
    """100 ta post borligini tekshirish — sekinroq"""
    javob = requests.get(f"{base_url}/posts")
    assert len(javob.json()) == 100