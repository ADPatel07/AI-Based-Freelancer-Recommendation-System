from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from F_Recommendation import *

app = FastAPI()

class Job(BaseModel):
    required_skills:str	
    budget:int	
    timeline_days:int

@app.post("/recommend/")
async def addImage(job:Job):
    res = recommend_freelancers(job.model_dump())
    return JSONResponse(res)