from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_picture = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jihane Jait"
PAGE_ICON = ":wave:"
NAME = "Jihane Jait"
Description = """
Environmental Analyst and Microbiologist with experience as a Front-end Developer
"""
EMAIL = "jihane.jaiit@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "https://www.linkedin.com/in/jait-jihane-125860206/",
    "Github": "https://github.com/Jaitjihane/Jaitjihane",
}
PROJECTS = {
    " 🚀 Chatbot- Answer basic questions"
    " 🚀 QuizApp - To test the knowledge on a particular topic"
    " 🚀 Data analysis project - Epidemiological study of tuberculosis in the province of Khemissset"
    " 🚀 Web scraping Tool- Scraping Data from websites like images, video etc"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_picture = Image.open(profile_picture)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_picture, width=170)

with col2:
    st.title(NAME)
    st.write(Description)
    st.download_button(
        label="📌 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/ octet-stream",
    )
    st.write("✉️", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✔️ Strong knowledge and background in microbiology and environmental sciences.
    - ✔️ 2 years experience as front-end developer.
    - ✔️ Strong hands and knowledge in HTML, CSS, Javascript and Python.
    - ✔️ Excellent team-player and displaying strong communication skills.
    - ✔️ Strong problem-solving and critical thinking skills
    - ✔️ Good understanding of statiscal principles and their applications.
    """
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard skills")
st.write(
    """
    - 💻 Programming: HTML, CSS, Javascript and Python(Pandas, Beautifulsoup).
    - 👨‍🔬 Microbiology techniques(Microscopy,Aseptic techniques, PCR,Microbial identification).
    - 💻 Frameworks: Django, Bootstrap 4, React js.
    - 👨‍💻 Data visualization: MS Excel, PowerBi,  Ms Access.
    """
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Professionnal experience")
st.write("---")

# ---Job I
st.write("👨‍💻", "**Front-end developer | Freelance**")
st.write(" January 2018 - March 2020")
st.write(
    """
    - ✔️ Used programming languages such as HTML, CSS, and Javascript to create functional user interfaces.
    - ✔️ Optimized sites for SEO.
    """
)

# ---Job II
st.write("👨‍🔬", "**Research Intern, Tuberculosis Laboratory**")
st.write("December 2019 - March 2020")
st.write(
    """
    - ✔️ Collected and analyzed data on the prevalence of tuberculosis in the Khemisset province using SPSS software.
    - ✔️ Developed an epidemiological study to evaluate risk factors related to tuberculosis in the region (SWOT Matrix).
    - ✔️ Performed diagnostic tests and laboratory analyses.
    """
)

# ---JOb III
st.write("👨‍🏫", "**Robotics Trainer, Robomakers Academy**")
st.write("August 2021 - January 2022")
st.write(
    """
    - ✔️ Design & delivery of robotics training for high school students & education professionals.
    - ✔️ Developed customized training materials, including manuals, presentations, and hands-on exercises, to meet the specific needs of each client.
    - ✔️ Trained over 150 individuals and teams, with a 95% success rate in achieving the learning objectives.
    - ✔️ Robotics training included: Scratch, Arduino and Python. 
    """
)
