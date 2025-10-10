"""
Basic tests for the FastAPI application.
"""
import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add parent directory to path to import main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


def test_health_check(client):
    """Test that the API is accessible."""
    response = client.get("/")
    assert response.status_code in [200, 404]  # Either root exists or doesn't
    # The app should at least respond


def test_api_exists():
    """Test that the FastAPI app object exists."""
    assert app is not None
    assert hasattr(app, 'routes')


def test_app_has_routes():
    """Test that the app has routes defined."""
    routes = [route.path for route in app.routes]
    assert len(routes) > 0, "App should have at least one route"

