API_KEY = [
    "a91e4bc5-cdfc-4e22-abc7-1c331e94d26e",  # use this one
    "64ed6fbe-a080-4c61-9f05-ec8f88fe4d54",
    "f1c37426-1c38-468b-a6f8-2a0c9bdcdce7",
]


USERNAME_QUERY="""
        query getUserQuestionStats($userSlug:String!){
            userProfileUserQuestionProgressV2(userSlug: $userSlug){
                numAcceptedQuestions{
                        difficulty
                        count
                        }
                }
            }
         """