"""
Database/State management for collecting user data
(In-memory for simplicity; can be replaced with actual DB later)
"""

# Store user conversation states
user_states = {}

class UserState:
    """Represents user state in form filling"""
    def __init__(self, user_id):
        self.user_id = user_id
        self.form_stage = None  # 'asking_name', 'asking_contact', 'asking_request'
        self.name = None
        self.contact = None
        self.request = None

def get_user_state(user_id):
    """Get or create user state"""
    if user_id not in user_states:
        user_states[user_id] = UserState(user_id)
    return user_states[user_id]

def reset_user_state(user_id):
    """Clear user state"""
    if user_id in user_states:
        del user_states[user_id]
