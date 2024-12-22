import requests
import json

def get_access_token(email, password):
    """Fetch the main profile access token."""
    login_url = "https://b-api.facebook.com/method/auth.login"
    params = {
        "email": email,
        "password": password,
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "format": "json",
        "sdk_version": "2",
        "generate_session_cookies": "1",
        "locale": "en_US",
        "sdk": "ios",
        "sig": "3f555f99fb61fcd7aa0c44f58f522ef6",
    }
    response = requests.get(login_url, params=params)
    data = response.json()
    if "access_token" in data:
        print("[✔] Main Profile Access Token Retrieved Successfully!")
        return data["access_token"]
    else:
        print("[✘] Login Failed! Please check email/password.")
        return None

def get_secondary_profiles(access_token):
    """Fetch secondary profiles linked to the main profile."""
    graph_url = f"https://graph.facebook.com/me?fields=profiles&access_token={access_token}"
    response = requests.get(graph_url)
    data = response.json()
    if "profiles" in data:
        profiles = data["profiles"]["data"]
        print("[✔] Secondary Profiles Found:")
        for profile in profiles:
            print(f"- Name: {profile['name']}, ID: {profile['id']}")
        return profiles
    else:
        print("[✘] No Secondary Profiles Found!")
        return []

def get_profile_tokens(main_access_token, profiles):
    """Retrieve access tokens for secondary profiles."""
    for profile in profiles:
        profile_id = profile["id"]
        profile_token_url = f"https://graph.facebook.com/{profile_id}/accounts?access_token={main_access_token}"
        response = requests.get(profile_token_url)
        profile_data = response.json()
        if "access_token" in profile_data:
            print(f"- Profile Name: {profile['name']}, Token: {profile_data['access_token']}")
        else:
            print(f"- Profile Name: {profile['name']}, Token: [Failed to Retrieve]")

if __name__ == "__main__":
    print("=== Facebook Secondary Profile Token Extractor ===")
    email = input("[📧] Enter Facebook Email/Phone: ")
    password = input("[🔑] Enter Facebook Password: ")

    main_access_token = get_access_token(email, password)

    if main_access_token:
        profiles = get_secondary_profiles(main_access_token)
        if profiles:
            print("\n[✔] Generating Tokens for Secondary Profiles...")
            get_profile_tokens(main_access_token, profiles)
        else:
            print("[✘] No Secondary Profiles Available!")
