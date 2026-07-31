from core.memory import get_preference
from core.memory import save_user_info, get_user_info
from core.memory import get_conversation
from core.personality import get_personality
from core.response import generate_response
from core.memory import save_preference, get_preference

def think(message):
    
    personality = get_personality()
    
    memories = get_conversation()
    
    message = message.lower()
    
    if "my name is" in message:
        
        name = message.replace("my name is", "").strip()
        
        save_user_info("name", name)
        
        return f"Nice to meet you, {name}!"
    
    if "what do i like" in message:
        
        hobby = get_preference("like")
        
        if hobby:
            return f"You like {hobby}."
        
        return "I don't know what you like yet."
    
    if "i like" in message:
        
        hobby = message.replace("i like", "").strip()
        
        save_preference("like", hobby)
        
        return f"I'll remember that you like {hobby}."
    
    if "hello" in message or "hi" in message:
        
        return generate_response(message)
    
    if "name" in message:
        return "My name is ALEX."
    
    if memories:
        return (
            "I remember our previous conversation."
            "I am always learning from our interactions."
        )
        
    return (
        f"I am{personality['name']}."
        "I am thinking about your request."
    )