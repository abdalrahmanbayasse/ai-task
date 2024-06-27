from django.shortcuts import render
from django.shortcuts import HttpResponse
from .api import txt_bot
import aiohttp

# Create your views here.


async def send_request(request):
    response = "Answer Goes Here"

    if request.method == "POST":
        question = request.POST.get("txt_send_ai")
        async with aiohttp.ClientSession() as session:
            response = await txt_bot(question=question)
            
    context = {"response": response}
    return render(request, "base.html", context)
