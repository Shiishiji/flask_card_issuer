from dotenv import load_dotenv


class DotenvAdapter:
    env_path: str

    def __init__(self):
        self.env_path = ".env"

    def load_env_file(self) -> None:
        load_dotenv(self.env_path, override=False)
