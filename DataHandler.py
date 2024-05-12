# write a ProfPrfile class to handle the data
from config import setting
from email.mime.text import MIMEText

class ProfProfile:
    def __init__(self, name, label, email, research_interests, university, publications=None):
        self.name = name
        self.label = label
        self.email = email
        self.research_interests = research_interests
        self.university = university
        self.publications = publications
    
    def __str__(self):
        return f"{self.name} ({self.email}) - {self.university}"
    
    def __repr__(self):
        return f"ProfProfile(name={self.name}, label={self.label}, email={self.email}, research_interests={self.research_interests}, university={self.university}, publications={self.publications})"
    
    def create_prompt(self):
        return f"Dear Professor {self.name},\n\nI am writing to express my interest in your research on {self.research_interests}. I am currently a student at {self.university} and would like to inquire about potential research opportunities with you. I have attached my CV and a list of my publications for your review. I would be grateful for the opportunity to discuss this further with you.\n\nThank you for your time and consideration.\n\nSincerely,\n{setting.NAME}\n"
    
    def store_email_content(self, message):
        msg = MIMEText(message)
        msg['Subject'] = self.name
        msg['From'] = setting.SENDER_EMAIL
        msg['To'] = self.email
        self.msg = msg
        return msg
    
    def generate_txt_for_email(self):
        dir = setting.OUTPUT_DIR
        filename = f"{self.name}.txt"
        with open(dir + filename, "w") as f:
            f.write(self.msg.as_string())
        return dir + filename

if __name__ == "__main__":
    # Example prof
    prof = ProfProfile(
        name="John Doe",
        label="Yes",
        email="dsafsa@gmail.com",
        research_interests=["Machine Learning", "Data Science"],
        university="University of Example",
        publications=["Publication 1", "Publication 2"]
    )

    print(prof)
    # print repr
    print(repr(prof))
