from core.personality import get_personality
from core.memory import get_user_info
import random

def generate_response(message):
    
    personality = get_personality()
    
    name = personality["name"]
    user_name = get_user_info("name")
    tone = personality["tone"]
    
    message = message.lower()
    
    greeting = [
        f"Hey! I'm {name}. Nice to meet talk with you.",
        f"Hello! I'm {name}. How cam I help you today?",
        f"Hi! Good to see you. what can we do together?"
    ]
    
    if "hello" in message or "hi" in message:
        
        if user_name:
            return f"Hey {user_name}! Nice to talk with you again."
        
        return random.choice(greetings)
        
    return f"Hello, I am {name}."
    
    if "how are you" in message:
        if tone == "friendly":
            return "I'm doing great! thanks for asking."
        
        return "I am working normally."
    
    if "who are you" in message:
        
        return (
            f"I am {name}, "
            "a personal AI assistant designed to help you."
        )
        
    return (
        f"I understand your message: {message}. "
        "I will try to help you."
    )