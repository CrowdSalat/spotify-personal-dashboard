import os

# read env variables or use default value if it does not find one
spotify_client_properties = {
    "client_id": os.getenv('SPOTIFY_CLIENT_ID', "4d3fc18d04dc466aa657d99e4cdf974a"),
    "secret_clientid": os.getenv('SPOTIFY_CLIENT_ID_SECRET', "a47e2d59fc0041d5ba6c2207e0998119"),
    "callback_url": os.getenv('SPOTIFY_CALLBACK_URL', "http://localhost:8080/albums")
}