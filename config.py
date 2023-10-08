import os

class ConfigObject():
    ISSERVER: bool = os.environ.get("secret_key") is str
    
    SECRET_KEY: str = "supersecretkey"

    def __init__(self):
        if self.ISSERVER:
            SECRET_KEY = os.environ.get("secret_key")
            
config = ConfigObject()