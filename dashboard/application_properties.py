import os

# read env variables or use default value if it does not find one
spotify_client_properties = {
    "client_id": os.getenv('SPOTIFY_CLIENT_ID', "<INVALID>"),
    "secret_clientid": os.getenv('SPOTIFY_CLIENT_ID_SECRET', "<INVALID>"),
    "callback_url": os.getenv('SPOTIFY_CALLBACK_URL', "http://localhost:8080/dashboard/albums")
}