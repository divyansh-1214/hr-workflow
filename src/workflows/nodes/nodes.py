from numbers import Number

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import HumanMessage, SystemMessage

from ..models import (
    Rating,
    Scores,
    Skills,
    llm,
    system_prompt_skills_extraction,
    system_prompt_skills_rating,
)
from ..state import ResumeState


def get_jd(state: ResumeState) -> dict:
    jd_text = state.get("jd_text")
    if jd_text is None:
        raise KeyError("jd_text is required")

    return {"jd_text": jd_text.strip()}


def extract_skill(state: ResumeState) -> dict:
    jd_text = state.get("jd_text")
    if jd_text is None:
        raise KeyError("jd_text is required")
    result = llm.with_structured_output(Skills).invoke(
        [
            SystemMessage(content=system_prompt_skills_extraction),
            HumanMessage(content=jd_text.strip()),
        ]
    )
    skills = result.skills
    if skills is None:
        raise KeyError("skills is required")

    return {"skills": skills}


def get_resume(state: ResumeState) -> dict:
    docs = PyPDFLoader("Divyansh_Resume.pdf").load()
    text = "\n".join(d.page_content for d in docs)
    if text is None:
        raise KeyError("resume_text is required")

    return {"resume_text": text.strip()}


def rate_resume(state: ResumeState) -> dict:
    resume_text = state.get("resume_text")
    if resume_text is None:
        raise KeyError("resume_text is required")
    skills = state.get("skills")
    if skills is None:
        raise KeyError("skills is required")
    rating = llm.with_structured_output(Scores).invoke(
        [
            SystemMessage(content=system_prompt_skills_rating),
            HumanMessage(content=resume_text.strip()),
            HumanMessage(content=", ".join(skills or [])),
        ]
    )
    print(rating.model_dump_json(indent=2))
    return {"scores": rating}
