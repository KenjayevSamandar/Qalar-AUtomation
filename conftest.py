import pytest

@pytest.fixture
def base_url():
	return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def yangi_post_data():
	return {
		"title":"Test post",
		"body":"Test matni",
		"userId":1
}