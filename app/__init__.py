from flask import Flask


class createApp(Flask):
    def __init__(self):
        from .routes import main
        
        super().__init__(__name__)    
        self.register_blueprint(main)
    
