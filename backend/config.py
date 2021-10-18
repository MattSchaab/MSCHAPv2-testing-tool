from pydantic import BaseSettings


class Settings(BaseSettings):
    RADIUS_HOST: str
    RADIUS_SECRET: str
    RADIUS_NAS_IP: str
    RADIUS_NAS_ID: str
    USERNAME: str
    PASSWORD: str

settings = Settings()