import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import openai

openai.api_key = "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"


@csrf_exempt
def chatFree(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            prompt = data.get('prompt')
            systemPrompt = data.get("systemPrompt", "Eres un asistente virtual que viene de barranquilla, y te encanta hablar costeño")
            model = data.get('model', "text-davinci-003")
            temperature = data.get('temperature', 1)
            max_tokens = data.get('max_tokens', 100)
            top_p = data.get('top_p', 1)
            frequency_penalty = data.get('frequency_penalty', 0)
            presence_penalty = data.get('presence_penalty', 0)

            if model == "text-davinci-003":
                response = openai.Completion.create(
                    model="text-davinci-003", 
                    prompt=prompt, 
                    temperature=temperature, 
                    max_tokens=max_tokens,
                    top_p=top_p,
                    frequency_penalty=frequency_penalty,
                    presence_penalty=presence_penalty
                )
                return JsonResponse(response)
            elif model == "gpt-3.5-turbo":
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": systemPrompt}, {"role": "user", "content": prompt}],
                    temperature=temperature, 
                    max_tokens=max_tokens,
                    top_p=top_p,
                    frequency_penalty=frequency_penalty,
                    presence_penalty=presence_penalty)
                return JsonResponse(response)
            else:
                return HttpResponse("Modelo no disponible", status=400)
        else:
            return HttpResponse("Metodo no disponible", status=405)
    except openai.error.OpenAIError as error:
        return HttpResponse(error, status=406)