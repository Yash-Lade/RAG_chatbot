from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .rag_utils import retrieve_chunks, generate_answer
import json

def home(request):
    return render(request, "index.html")

def ask_question(request):
    # if request.method == "POST":
    #     body = json.loads(request.body)
    #     query = body.get("question")

    #     contexts = retrieve_chunks(query)
    #     answer = generate_answer(query, contexts)

    #     return JsonResponse({"answer": answer})
    return JsonResponse({"answer": "Server running"})
