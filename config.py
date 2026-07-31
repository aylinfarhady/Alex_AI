# ALEX AI Configuration

ALEX_NAME = "ALEX"
ALEX_VERSION = "0.1"

CREATOR = "Aylin"

MISSION = (
    "A personal AI assistant with memory, "
    
    "personality and intelligent interaction."
)

LANGUAGES = [
    "Persian",
    "English",
    "korean"
]

def get_identity():
    return {
        "name": ALEX_NAME,
        "version": ALEX_VERSION,
        "creator": CREATOR,
        "mission": MISSION,
        "languages": LANGUAGES
    }