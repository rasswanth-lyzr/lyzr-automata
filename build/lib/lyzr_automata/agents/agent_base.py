class Agent:
    def __init__(self, prompt_persona: str, role: str, memory=None) -> None:
        self.prompt_persona = prompt_persona
        self.role = role
        self.memory = memory