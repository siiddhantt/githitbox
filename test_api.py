import requests
import time


def test_profile_counter():
    base_url = "http://localhost:8000"
    test_username = "testuser"

    print("🧪 Testing GitHitBox...")

    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        assert response.status_code == 200
        print("✅ Health check passed")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return

    print("\n2. Testing root endpoint...")
    try:
        response = requests.get(base_url)
        assert response.status_code == 200
        data = response.json()
        assert "service" in data
        print("✅ Root endpoint working")
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")
        return

    print(f"\n3. Testing badge generation for '{test_username}'...")
    try:
        response = requests.get(f"{base_url}/badge/{test_username}")
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/png"
        print("✅ Badge generation successful")
    except Exception as e:
        print(f"❌ Badge generation failed: {e}")
        return

    print(f"\n4. Testing count endpoint for '{test_username}'...")
    try:
        response = requests.get(f"{base_url}/count/{test_username}")
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == test_username
        assert data["count"] >= 1
        print(f"✅ Count endpoint working - Current count: {data['count']}")
    except Exception as e:
        print(f"❌ Count endpoint failed: {e}")
        return

    print(f"\n5. Testing counter increment...")
    try:
        response = requests.get(f"{base_url}/count/{test_username}")
        initial_count = response.json()["count"]

        requests.get(f"{base_url}/badge/{test_username}")

        response = requests.get(f"{base_url}/count/{test_username}")
        new_count = response.json()["count"]

        assert new_count > initial_count
        print(
            f"✅ Counter increment working - Count increased from {initial_count} to {new_count}"
        )
    except Exception as e:
        print(f"❌ Counter increment failed: {e}")
        return

    print(f"\n6. Testing global stats...")
    try:
        response = requests.get(f"{base_url}/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_profiles" in data
        assert "total_hits" in data
        print(
            f"✅ Global stats working - Profiles: {data['total_profiles']}, Hits: {data['total_hits']}"
        )
    except Exception as e:
        print(f"❌ Global stats failed: {e}")
        return

    print(f"\n7. Testing badge styles...")
    styles = ["flat", "plastic", "counter", "for-the-badge"]
    for style in styles:
        try:
            response = requests.get(f"{base_url}/badge/{test_username}?style={style}")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            print(f"✅ Style '{style}' working")
        except Exception as e:
            print(f"❌ Style '{style}' failed: {e}")

    print("\n🎉 All tests passed! The profile counter is working correctly.")
    print(f"\n📋 Example usage in README.md:")
    print(f"![Profile Views](http://localhost:8000/badge/{test_username})")
    print(f"\n🔗 View your badge at: http://localhost:8000/badge/{test_username}")


if __name__ == "__main__":
    test_profile_counter()
