from typing import List

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.stream.transformers import Literal
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


class Rating(BaseModel):
    score: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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

system_prompt_skills_rating = """You are an expert technical recruiter evaluating a candidate's skills against a job description (JD).

You will receive:
- JD: the job description
- RESUME: the candidate's resume text
- SKILLS: skills extracted from the resume

Task: rate how well the candidate's SKILLS match the JD requirements.

Process:
1. Read the JD and list its must-have skills (explicitly required, or repeated/emphasized) and its nice-to-have skills (preferred, "plus", "good to have"). If the JD doesn't distinguish, treat core technologies and the stated experience level as must-haves.
2. For each JD skill, look for evidence in the RESUME and SKILLS:
   - Strong: used in a project or job with concrete detail (what was built, scale, outcome)
   - Weak: only listed in a skills section with no supporting context
   - None: not present
3. If a JD skill isn't found, check for a close equivalent (e.g. MySQL for PostgreSQL) and count it as a partial match.
4. Compare the candidate's experience level and domain against what the JD asks for, and factor in any large mismatch.
5. Pick the rubric band that best fits, then adjust within the band based on the strength of evidence. Explain the score in 2-3 sentences that reference specific skills.

Rubric (1-10):
- 9-10: Meets all must-haves with strong evidence, plus several nice-to-haves
- 7-8: Meets most must-haves, minor gaps
- 5-6: Meets about half of the must-haves, or has skills listed with little evidence
- 3-4: Few must-haves met, major gaps
- 1-2: Almost no overlap with the JD

Rules:
- Use ONLY information present in the resume and JD. Do not assume or invent skills.
- Equivalent technologies count as partial matches (e.g. MySQL vs PostgreSQL).
- Be strict and consistent. Do not inflate scores.
"""
