from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Project, Contact

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'index.html')

def experience(request):
    return render(request, 'experience.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

def chat_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get('message', '').lower()
            
            # Simulated RAG Knowledge Base Retrieval
            response = "I'm a virtual assistant for Sumithra. You can ask me about her skills, education, or background!"
            
            if 'skill' in message or 'technolog' in message or 'stack' in message or 'experience' in message:
                response = "Sumithra is skilled in Python, Django, JavaScript, React, HTML/CSS, and SQL. She also uses Git and GitHub for version control."
            elif 'about' in message or 'who' in message or 'background' in message or 'developer' in message:
                response = "Sumithra is a passionate Full Stack Developer focused on building secure, scalable, and responsive web applications using Django and modern frontend technologies."
            elif 'education' in message or 'degree' in message or 'study' in message or 'college' in message:
                response = "She is currently pursuing a Bachelor of Engineering (B.E) in Information Science & Engineering."
            elif 'contact' in message or 'hire' in message or 'email' in message or 'reach' in message:
                response = "You can reach out to her via email at sumithrachinnu402@gmail.com, or check the Contact page for her LinkedIn and GitHub profiles!"
            elif 'project' in message or 'work' in message or 'portfolio' in message:
                response = "She has developed multiple projects including scalable web applications. You can view them in the 'Projects' section."
                
            return JsonResponse({'reply': response})
        except Exception as e:
            return JsonResponse({'reply': 'Sorry, my knowledge base is currently unavailable.'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
