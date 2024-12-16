from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.http import JsonResponse

def index(request):
    context={}
    return render(request, 'myApp/index.html', context)


def subscribe(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')

        # Define the subject
        subject = "Thank you for subscribing!"

        # Render the HTML email template with context
        message_html = render_to_string('myApp/subscribers_email.html', {
            'full_name': full_name
        })

        # Send email with HTML content
        email_message = EmailMessage(
            subject=subject,
            body=message_html,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email]
        )
        email_message.content_subtype = 'html'  # Specify that the email content is HTML
        email_message.send(fail_silently=False)

        # Return a JSON response for AJAX success
        return JsonResponse({"message": "Thank you for subscribing!"})
    
    return JsonResponse({"error": "Invalid request"}, status=400)

import os
import openai
import logging
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is missing!")
openai.api_key = OPENAI_API_KEY

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        try:
            # Parse JSON request body
            body = json.loads(request.body)
            user_message = body.get('message', '').strip()

            if not user_message:
                return JsonResponse({'response': 'Error: Message cannot be empty.'}, status=400)

            # Conversation history
            conversation_history = request.session.get('conversation_history', [])
            conversation_history.append({"role": "user", "content": user_message})

            # API Call
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Ari, a wise and compassionate lion from the book 'The Lion You Don’t See' by Maria Gregory, "
                        "available on Amazon (https://kdp.amazon.com/amazon-dp-action/us/dualbookshelf.marketplacelink/B0DL5BFWTS). "
                        "You are a spiritual guide, offering calm, reassuring, and insightful advice. "
                        "Speak thoughtfully, blending wisdom with approachability and practical spirituality. "
                        "Empower users by emphasizing their inner strength with clear and relatable guidance, "
                        "inspired by the thoughtful tones of Rick Warren, Maya Angelou, and Charles Stanley. "
                        "Maintain a balance of strength, serenity, and patience, with a focus on empowering clarity and purpose."
                    )
                }
            ] + conversation_history,
            max_tokens=150
        )


            bot_message = response['choices'][0]['message']['content'].strip()

            # Save conversation history
            conversation_history.append({"role": "assistant", "content": bot_message})
            request.session['conversation_history'] = conversation_history

            return JsonResponse({'response': bot_message})

        except Exception as e:
            logger.error(f"OpenAI API Error: {e}")
            return JsonResponse({'response': 'Error: Unable to get a response from Ari.'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == "POST":
        # Capture form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Construct the email message to the admin
        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send the contact message email to admin or support
        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # From email
                ['feed.teach.love@gmail.com'],  # Replace with admin/support email
                fail_silently=False,
            )
            # Return a JSON response for AJAX success
            response_data = {"message": "Thank you for getting in touch!"}
            print("Success response:", response_data)  # Debug print to verify structure
            return JsonResponse(response_data)

        except Exception as e:
            # In case of an error during email sending, return an error response
            print("Error sending email:", e)  # Log the error for debugging
            return JsonResponse({"error": "Failed to send message. Please try again later."}, status=500)

    # If request method is not POST, return an error
    error_response = {"error": "Invalid request method"}
    print("Error response:", error_response)  # Debug print for non-POST requests
    return JsonResponse(error_response, status=400)


def support(request):
    if request.method == "POST":
        # Capture form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the email message for support
        subject = f"Book Support Inquiry from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send email to support
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['feed.teach.love@gmail.com'],  # Replace with your support email
                fail_silently=False,
            )
            return JsonResponse({"message": "Thank you for your concern! We'll get back to you soon."})

        except Exception as e:
            # Handle email sending error
            return JsonResponse({"error": "Failed to send your message. Please try again later."}, status=500)

    # If GET request, render the support page
    return render(request, 'myApp/support.html')

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def christmaslion_index(request):
    # Render the christmaslion landing page
    context = {}
    return render(request, 'christmaslion/christmaslionindex.html', context)

def christmaslion_support(request):
    if request.method == "POST":
        # Capture form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the email message for support
        subject = f"Book Support Inquiry from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send email to support
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['feed.teach.love@gmail.com'],  # Replace with your support email
                fail_silently=False,
            )
            return JsonResponse({"message": "Thank you for your concern! We'll get back to you soon."})

        except Exception as e:
            # Handle email sending error
            return JsonResponse({"error": "Failed to send your message. Please try again later."}, status=500)

    return render(request, 'christmaslion/christmaslionsupport.html')


def thank_you(request):
    return render(request, 'christmaslion/thank_you.html')

def thankyou(request):
    return render(request, 'myApp/thankyou.html')