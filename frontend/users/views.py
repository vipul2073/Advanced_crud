from django.shortcuts import render, redirect
from django.conf import settings
import requests

API_URL = "http://127.0.0.1:5000/api/users"

def index(request):
    if request.method == "POST":
        action = request.POST.get("action")

        # --- ADD ---
        if action == "add":
            username = request.POST.get("username")
            email = request.POST.get("email")
            if username and email:
                requests.post(API_URL, json={"username": username, "email": email})

        # --- DELETE ---
        elif action == "delete":
            user_id = request.POST.get("user_id")
            if user_id:
                requests.delete(f"{API_URL}/{user_id}")

        # --- UPDATE ---
        elif action == "update":
            user_id = request.POST.get("user_id")
            username = request.POST.get("username")
            email = request.POST.get("email")
            if user_id:
                requests.put(f"{API_URL}/{user_id}", json={"username": username, "email": email})

        return redirect("/")   # refresh page

    # Fetch all users
    try:
        users = requests.get(API_URL).json()
    except:
        users = []

    return render(request, "index.html", {"users": users})
