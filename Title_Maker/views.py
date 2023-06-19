from django.shortcuts import render
import openai
openai.api_key = 'YOUR_API_KEY'

def generate_title(description):
    prompt = f"Video description: {description}\nSuggested title:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
    )
    suggested_title = response.choices[0].message.content.replace("Assistant:", "").strip()
    return suggested_title

def generate_title_view(request):
    if request.method == 'POST':
        description = request.POST.get('description', '')
        suggested_title = generate_title(description)
        return render(request, 'result.html', {'suggested_title': suggested_title})
    return render(request, 'form.html')
