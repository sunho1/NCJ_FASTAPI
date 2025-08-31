from fastapi import APIRouter


router = APIRouter(
    prefix= "/auth" ,
    tags = ["유저 인증 API"]
)

@router.get("/login", tags=['로그인'])
async def user_auth() :
    return [{"user" : "sunho"} , {"password" : "pass_complete"}]


@router.post("/signup" , tags=["회원가입"])
def user_signup() :
    return [{"message:":"회원가입"}]
