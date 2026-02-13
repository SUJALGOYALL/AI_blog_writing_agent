import os
import requests


def generate_image_bytes(prompt: str) -> bytes:
    api_key = os.environ.get("A4F_API_KEY")
    if not api_key:
        raise RuntimeError("A4F_API_KEY not set")

    resp = requests.post(
        "https://api.a4f.co/v1/images/generations",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "provider-4/imagen-3.5",
            "prompt": prompt,
        },
        timeout=60,
    )

    data = resp.json()
    url = data["data"][0].get("url")
    if not url:
        raise RuntimeError("No image URL returned")

    return requests.get(url).content
