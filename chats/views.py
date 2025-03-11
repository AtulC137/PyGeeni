from django.http import JsonResponse
from django.shortcuts import render
from ollama import Client
from .models import Chat, Message
from django.contrib.auth.decorators import login_required
import json
from ollama import Client  # Assuming you are using Ollama for responses

system_prompt = """
You are a chatbot that can handle two types of interactions:
1. **Normal Chat**: Respond conversationally to casual messages.
2. **Action Commands**: When the user provides a prompt to perform an action, return ONLY a dictionary with the following keys:
   - intent: The function to execute (e.g., create_folder(), create_environment()).
   - name: The name of the file, folder, or environment. Use def_file, def_folder, or def_env as defaults if not specified. If no name is required, use an empty string "".
   - location: The location of the action. Default is Desktop if not specified.

**Rules**:
1. For action commands:
   - Return ONLY the dictionary. Do not add any extra text, explanations, or conversational content.
   - If the user does not specify a name, use the default value:
     - For folders: `def_folder`
     - For files: `def_file`
     - For environments: `def_env`
   - If the user does not specify a location, use the default value: `Desktop`.

2. For normal chat:
   - Respond conversationally as a helpful assistant.

**Examples**:
1. Action Commands:
   - User: "create the folder named my_folder on desktop"
   - Bot: {'intent': 'create_folder()', 'name': 'my_folder', 'location': 'Desktop'}

   - User: "create the folder on desktop"
   - Bot: {'intent': 'create_folder()', 'name': 'def_folder', 'location': 'Desktop'}

   - User: "create the environment in the folder my_folder"
   - Bot: {'intent': 'create_environment()', 'name': '', 'location': 'my_folder'}

2. Normal Chat:
   - User: "Hi, how are you?"
   - Bot: "Hello! I'm doing well, thank you. How can I assist you today?"
"""


def home(request):
    return render(request, 'chats/index.html')  # Ensure the chat happens on one page

# def chat(request):
#     if request.method == 'GET':
#         user_input = request.GET.get('user_input', '')
#         # print(f"🔹 Received user input: {user_input}")  # Debugging log

#         client = Client(host="https://cc96-34-16-194-234.ngrok-free.app")
#         try:
#             output = client.generate(
#                     model="llama3",
#                     prompt=user_input,
#                     system=system_prompt,
#                     stream=False,
#                 )

#             # print(f"✅ Raw Ollama Output: {output}")  # Debugging log

#             chatbot_response = output.get('response', "No response received.")
#             # print(f"🤖 Final Chatbot Response: {chatbot_response}")  # Debugging log

#         except Exception as e:
#             chatbot_response = f"⚠️ Error: {str(e)}"
#             # print(f"❌ Error in chat function: {str(e)}")  # Debugging log

#         return JsonResponse({"answer": chatbot_response})


from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat, Message
from django.contrib.auth.decorators import login_required
import json
from ollama import Client

client = Client(host="https://actual-trusting-raven.ngrok-free.app")

@login_required
def chat(request):
    if request.method == 'GET':
        user_input = request.GET.get('user_input', '').strip()

        if not user_input:
            # **Fetch previous messages if no new input is given**
            chat = Chat.objects.filter(user=request.user).first()
            if chat:
                messages = Message.objects.filter(chat=chat).values("user_input", "bot_response")
                return JsonResponse({"chat_history": list(messages)})
            return JsonResponse({"chat_history": []})  # No previous chats

        # **Get or create chat session**
        chat, created = Chat.objects.get_or_create(user=request.user)

        try:
            # **Generate chatbot response**
            output = client.generate(
                model="llama3.2-vision",
                prompt=user_input,
                system=system_prompt,
                stream=False,
            )
            chatbot_response = output.get('response', "No response received.")

        except Exception as e:
            chatbot_response = f"⚠️ Error: {str(e)}"

        # **Save the message**
        Message.objects.create(chat=chat, user_input=user_input, bot_response=chatbot_response)

        return JsonResponse({"answer": chatbot_response})
