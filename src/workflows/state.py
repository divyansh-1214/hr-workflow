from typing import Dict, List, TypedDict


class ResumeState(TypedDict, total=False):
    jd_text: str
    skills: List[str]
    resume_path: str
    resume_text: str
    scores: Dict[str, int]  # e.g. {"skill_match": 8, "experience": 6, ...}
    summary: str
