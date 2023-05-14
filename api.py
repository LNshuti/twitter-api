# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the API endpoint
API_ENDPOINT = "https://api.twitter.com/1.1/users/show.json?screen_name="

# Define the function to send a password reset email
def send_password_reset_email(username):
    # Make a request to the API endpoint
    response = requests.get(API_ENDPOINT + username)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response
        data = response.json()

        # Get the email address
        email_address = data["email"]

        # Send the password reset email
        send_email(email_address)

    else:
        # Raise an error
        raise Exception("Request failed with status code: " + str(response.status_code))

# Define the function to send an email
def send_email(email_address):
    # Create a message
    message = MailMessage()
    message.set_from("noreply@example.com")
    message.set_to(email_address)
    message.set_subject("Password Reset")
    message.set_body("Click here to reset your password: " + "https://twitter.com/password/reset")

    # Send the message
    smtp.send_message(message)

# Define the test function
def test_send_password_reset_email():
    # Try to send a password reset email to a valid user
    send_password_reset_email("username")

    # Assert that the email was sent
    assert len(mail.outbox) == 1

# Deploy the API endpoint
if __name__ == "__main__":
    # Create a FastAPI app
    app = FastAPI()

    # Add a route to send a password reset email
    @app.get("/reset-password/{username}")
    def reset_password(username: str):
        send_password_reset_email(username)

    # Start the app
    app.run()