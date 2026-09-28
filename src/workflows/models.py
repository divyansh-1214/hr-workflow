from typing import List

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

load_dotenv()


class Skills(BaseModel):
    skills: List[str]


class Scores(BaseModel):
    skill_match: int = Field(ge=0, le=10)
    experience: int = Field(ge=0, le=10)
    projects: int = Field(ge=0, le=10)
    education: int = Field(ge=0, le=10)
    overall: int = Field(ge=0, le=100)
    reasoning: str


llm = init_chat_model("google_genai:gemini-3.5-flash-lite", temperature=0.7)

system_prompt_skills_extraction = """
You are an expert technical recruiter and job description analyzer.

Your task is to extract all relevant skills from the provided job description.

Instructions:
1. Extract only skills explicitly mentioned or strongly implied.
2. Include programming languages, frameworks, databases, cloud platforms,
   DevOps tools, architectural concepts, and domain knowledge.
3. Include relevant engineering and interpersonal skills.
4. Avoid duplicate skills.
5. Do not invent technologies that are not supported by the JD.
6. Return concise, standardized skill names.
7. Follow the provided structured output schema.
"""
