import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    
    if not os.path.exists(MEMORY_FILE):
        return {}
    
    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)
        
def remember(category, key, value):
    
    memory = load_memory()
    
    if category not in memory:
        memory[category] = {}
        
    memory[category] [key] = value
    
    save_memory(memory)
    
def recall(category, key):
    
    memory = load_memory()
    
    if category not in memory:
        return None
    
    return memory[category].get(key)

def save_conversation(message):
    
    memory = load_memory()
    
    if "conversation" not in memory:
        memory["conversation"] = []
        
        memory["conversation"].append(message)
        
        save_memory(memory)
        
def get_conversation():
    
    memory = load_memory()
    
    return memory.get("conversation", [])

def save_user_info(key, value):
    
    memory = load_memory()
    
    if "user" not in memory:
        memory["user"] = {}
        
    memory["user"] [key] = value
    
    save_memory(memory)
    
def get_user_info(key):
    
    memory = load_memory()
    
    if "user" not in memory:
        return None 
    
    return memory["user"].get(key)

def save_preference(key, value):
    
    memory = load_memory()
    
    if "preference" not in memory:
        memory["preference"] = {}
        
    memory["preference"][key] = value
    
    save_memory(memory)
    
def get_preference(key):
    
    memory = load_memory()
    
    if "preferences" not in memory:
        return None
    
    return memory["preferences"].get(key)

    
