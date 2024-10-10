import weaviate, os
from weaviate.classes.init import Auth

# Best practice: store your credentials in environment variables
http_host = "localhost"
grpc_host = "localhost"
# weaviate_api_key = os.environ["WCD_DEMO_RO_KEY"]

client = weaviate.connect_to_custom(
    http_host=http_host,        # Hostname for the HTTP API connection
    http_port=8080,              # Default is 80, WCD uses 443
    http_secure=False,           # Whether to use https (secure) for the HTTP API connection
    grpc_host=grpc_host,        # Hostname for the gRPC API connection
    grpc_port=50051,              # Default is 50051, WCD uses 443
    grpc_secure=False         # Whether to use a secure channel for the gRPC API connection
    # auth_credentials=Auth.api_key(weaviate_api_key),  # API key for authentication
)

print(client.is_ready())