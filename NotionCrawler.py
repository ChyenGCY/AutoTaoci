import requests
from DataHandler import ProfProfile


class NotionAPIClient:
    def __init__(self, integration_token):
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {integration_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def query_database(self, database_id):
        url = f"{self.base_url}/databases/{database_id}/query"
        response = requests.post(url, headers=self.headers)
        response.raise_for_status()  # Raise an exception for error responses
        return response.json()


class NotionDatabaseRetriever:
    def __init__(self, integration_token, database_id):
        self.client = NotionAPIClient(integration_token)
        self.database_id = database_id

    def retrieve_database_content(self):
        response = self.client.query_database(self.database_id)
        results = response.get("results")
        return results

    def retrieve_profiles(self):
        profiles = []
        for row in self.retrieve_database_content():
            try:
                name = (
                    row.get("properties").get("Name").get("title")[0].get("plain_text")
                )
                label = (
                    row.get("properties").get("Label").get("select").get("name")
                    == "Yes"
                )
                email = row.get("properties").get("Email").get("email")
                research_interests = (
                    row.get("properties")
                    .get("ResearchInterest")
                    .get("rich_text")[0]
                    .get("plain_text")
                )
                university = (
                    row.get("properties").get("University").get("select").get("name")
                )
                if label:
                    profile = ProfProfile(
                        name, label, email, research_interests, university
                    )
                    profiles.append(profile)
            except Exception as e:
                print(f"Error processing row. Error: {e}")
        return profiles


# Example usage:
if __name__ == "__main__":
    integration_token = ""
    database_id = ""

    retriever = NotionDatabaseRetriever(integration_token, database_id)
    profiles = retriever.retrieve_profiles()

    for profile in profiles:
        print(profile)
