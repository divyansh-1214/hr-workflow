from dotenv import load_dotenv

from src.workflows.graph import graph

load_dotenv()

jd = """
    About the Role :
    As a Staff Software Engineer at Innovaccer, you'll be a senior technical leader who stays deep in the code.
    You'll personally design and build complex, high-impact parts of our platform - backend services, data pipelines, and the AI/ML-powered features that increasingly define our products - while setting the technical direction for your team or domain.
    This is a builder's role first: you'll write production code, own components end to end, and lead by doing, while also shaping architecture and mentoring the engineers around you.
    You'll work closely with product, clinical, and engineering peers to turn ambitious healthcare goals into robust, scalable software that ships.
    If you want to operate at Staff scope without stepping away from the keyboard, this role is for you.
    A day in the Life :
    - Design, build, and ship complex, critical components of Innovaccer's platform - backend services, APIs, and data pipelines - writing high-quality production code yourself
    - Build AI/ML-powered product features end to end: integrating models, designing the systems and data flows around them, and ensuring they perform reliably in production
    - Drive technical design for systems within your team or domain, making hands-on decisions for scalability, performance, security, and cost, then implementing them
    - Model engineering best practices across the SDLC - code quality, testing, security, observability, and operational excellence - and raise the bar through the code you write and review
    - Build resilient, well-tested services that integrate cleanly across products and with external healthcare systems
    - Ensure the software you build complies with healthcare and data-protection requirements, including HIPAA and GDPR, embedding compliance and security into the implementation
    - Debug, profile, and harden production systems, taking ownership of reliability and incident response for the systems you build
    - Provide hands-on technical mentorship to engineers through design reviews, pairing, and code review
    - Partner with product and clinical stakeholders to turn real-world needs into well-scoped, technically sound designs you can deliver
    - Evaluate and recommend technologies, frameworks, and tooling for your team, balancing capability, cost, risk, and time-to-value
    What You Need :
    - Bachelor's, Master's, or Ph. in Computer Science, Software Engineering, or a related field, or equivalent practical experience
    - 7+ years of software engineering experience with a strong track record of personally building and shipping production systems
    - Deep, current, hands-on coding expertise in one or more modern languages (e. , Python, Java, Go, or similar) - this role writes code daily
    - Strong software design skills across distributed systems, backend services, APIs, and data-intensive architectures
    - Experience building and integrating AI/ML into products - connecting models to real systems, handling data flows, and operationalizing them in production (you don't need to be a research scientist, but you should be comfortable building AI/ML-powered features)
    - Hands-on experience operating production systems : CI/CD, infrastructure-as-code, monitoring, performance tuning, and incident response
    - Familiarity with healthcare data standards (e. , FHIR, HL7) and regulatory compliance (HIPAA, GDPR), or the ability to ramp quickly on a regulated domain
    - Strong problem-solving skills and clear communication, with the ability to align engineers and stakeholders around a technical approach
    - Strong experience with cloud platforms (AWS, GCP, or Azure) and containerization/orchestration (Docker, Kubernetes
"""
# print(jd)
def main() -> None:
    result = graph.invoke({"jd_text": jd})
    print("Extracted skills:")
    for skill in result["skills"]:
        print(f"- {skill}")


if __name__ == "__main__":
    main()
