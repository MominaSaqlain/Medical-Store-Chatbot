from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from .ai_engine import get_bot_response

@xframe_options_exempt  # 👈 ADD THIS DECORATOR
def chatbot_view(request):
    user_input = ""
    response = ""
    
    if request.method == "POST":
        user_input = request.POST.get("message")
        response = get_bot_response(user_input)
    
    return render(request, "chatbot/ai_chatbot.html", {
        "user_input": user_input,
        "response": response
    })