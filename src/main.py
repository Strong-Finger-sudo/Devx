from fastapi import FastAPI
import os

from questions.router import router as question_router

app = FastAPI(
	title="Question",
)

app.include_router(question_router)