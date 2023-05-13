import json
from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
    
app = FastAPI()

class Username(BaseModel):
    username: str

@app.get("/")
def root():
    return {"message": "Welcome to the Twitter Password Reset API."}

@app.get("/send-reset-email")
def send_reset_email(username: Username):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Replace the following path with the correct path to your ChromeDriver executable
    service = Service("/path/to/chromedriver")

    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get("https://twitter.com/account/begin_password_reset")
        username_field = driver.find_element(By.NAME, "account_identifier")
        username_field.send_keys(username.username)
        username_field.send_keys(Keys.RETURN)

        # Perform additional actions if necessary, such as verifying the email was sent

    return {"message": f"Reset email sent to {username.username}"}


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

