import time

import requests
from fastapi import APIRouter, Depends
from sqlalchemy import select

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from questions.models import Question

router = APIRouter(
	prefix="/questions",
	tags=["questions"]
)

@router.post("/")
async def post_questions(question_number: int, session: AsyncSession = Depends(get_async_session)):
	unique_questions = []
	while question_number != 0:
		questions = requests.get(f"https://jservice.io/api/random?count={question_number}").json()

		for question in questions:
			question_data = Question(question_id=question["id"],
									question_text=question["question"],
									question_answer=question["answer"],
									question_created_at=time.strftime("%Y-%m-%d %H:%M:%S"))

			try:
				session.add(question_data)
				await session.commit()
				unique_questions.append(question_data.question_text)
				question_number -= 1

			except:
				await session.rollback()
	return unique_questions


@router.get("/")
async def get_questions(session: AsyncSession = Depends(get_async_session)):
	query = select(Question).where(Question.question_id > 0)

	result = await session.execute(query)

	return {
		'status': 200,
		'questions': result.scalars().all(),
		"details": "ok",
	}