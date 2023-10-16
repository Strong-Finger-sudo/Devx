from sqlalchemy import Column, Integer, String, TIMESTAMP

from database import Base

class Question(Base):
	__tablename__ = "questions"

	id = Column(Integer, primary_key=True, index=True)
	question_id = Column(Integer, unique=True)
	question_text = Column(String)
	question_answer = Column(String)
	question_created_at = Column(String)
