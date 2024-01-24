class ChatCommand:
    content: str
    user_id: str

    def __init__(self, content: str, user_id: str):
        self.content = content
        self.user_id = user_id