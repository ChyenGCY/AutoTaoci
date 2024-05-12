import warnings
warnings.filterwarnings("ignore")

from config import setting
from NotionCrawler import NotionDatabaseRetriever
from DataHandler import ProfProfile
from AI import GoogleGPT
from EmailSender import EmailSender

if __name__ == "__main__":
    if setting.READ_NOTION:
        retriever = NotionDatabaseRetriever(setting.INTEGRATION_TOKEN, setting.DATABASE_ID)
        profiles = retriever.retrieve_profiles()
    print(f"Retrieved {len(profiles)} profiles from Notion")

    if setting.AI_ENABLED:
        gpt = GoogleGPT(setting.GPT_API)
        prompt = setting.PROMPT_AIM
        my_bg = setting.PROMPT_MYBG
        extra_prompt = setting.EXTRA_PROMPT
        for profile in profiles:
            message = profile.create_prompt() + prompt + my_bg + extra_prompt
            response = gpt.send_message(message)
            profile.store_email_content(response)
            out = profile.generate_txt_for_email()
            print(f"Generated email content for {profile.name}, stored in {out}")

    if setting.SEND_EMAIL:
        sender = EmailSender(setting.SENDER_EMAIL, setting.SENDER_PASSWORD)
        for profile in profiles:
            sender.send_email(profile.msg, profile.email)
            print(f"Email sent to {profile.email}")

