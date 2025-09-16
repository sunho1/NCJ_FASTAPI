from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "root"
    DB_PASSWORD: str = "password"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_NAME: str = "mydb"

    class Config:
        env_file = ".env"   # .env 파일에서 불러오기 (선택)

settings = Settings()
