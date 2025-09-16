from fastapi import APIRouter


router = APIRouter(
    prefix= "/profile" ,
    tags = ["유저 프로필 API"]
    
)

@router.get("/get", tags=['get'])
async def user_auth() :
    return [{"type" : "get"} , {"password" : "pass_complete"}]


@router.post("/post" , tags=["회원가입"])
def user_signup() :
    return [{"type:":"post"}]


