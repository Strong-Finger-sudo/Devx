from datetime import datetime

from pydantic import BaseModel

class QuestionData(BaseModel):
	question_id: int
	question_text: str
	question_answer: str
	question_created_at: str