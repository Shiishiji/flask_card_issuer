class OrderCardDto:
    name: str
    color: str

    def to_json(self) -> str:
        return "{" + ('"name": "{}", "color": "{}"'.format(self.name, self.color)) + "}"
