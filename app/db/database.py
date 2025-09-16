from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , Session

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/mydb"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 의존성 주입용 함수
def get_db() -> Session:
    db = SessionLocal()
    try:
        # yield를 써야, 커넥션 쓰고 돌아와서 finally 함수 사용 가능
        yield db
    finally:
        db.close()
