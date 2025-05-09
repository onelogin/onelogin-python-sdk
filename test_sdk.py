import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Simple test to check if the SDK can be imported and basic objects can be created
print("SDK Import Test")
print(f"SDK Version: {onelogin.__version__}")

# Test creating configuration
print("\nTesting Configuration creation")
try:
    configuration = onelogin.Configuration(
        host="https://example.onelogin.com"
    )
    print("✅ Configuration created successfully")
except Exception as e:
    print(f"❌ Failed to create configuration: {e}")

# Test API client creation
print("\nTesting ApiClient creation")
try:
    api_client = onelogin.ApiClient(configuration)
    print("✅ ApiClient created successfully")
except Exception as e:
    print(f"❌ Failed to create ApiClient: {e}")

# Test API instance creation
print("\nTesting API instance creation")
try:
    users_api = onelogin.UsersV2Api(api_client)
    oauth_api = onelogin.OAuth2Api(api_client)
    print("✅ API instances created successfully")
except Exception as e:
    print(f"❌ Failed to create API instances: {e}")

# Test model creation
print("\nTesting model creation")
try:
    user = onelogin.User(
        email="test@example.com",
        firstname="Test",
        lastname="User"
    )
    print("✅ User model created successfully")
    print(f"User data: {user.model_dump()}")
except Exception as e:
    print(f"❌ Failed to create User model: {e}")

print("\nBasic SDK functionality test completed!")