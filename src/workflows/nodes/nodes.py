from langchain_core.messages import HumanMessage, SystemMessage

from ..models import Skills, llm, system_prompt_skills_extraction
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
    resume_text = state.get("resume_text")
    if resume_text is None:
        raise KeyError("resume_text is required")

    return {"resume_text": resume_text.strip()}
