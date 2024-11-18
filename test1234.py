import random
import seleniumbase
import self

"""
class TestRegisterAndApply(BaseCase):

    def generate_random_data(self):
        return {
            "first_name": f"First{random.randint(1000, 9999)}",
            "last_name": f"Last{random.randint(1000, 9999)}",
            "email": f"test{random.randint(1000, 9999)}@example.com",
            "password": "SecureP@ssw0rd123",
            "phone": f"010{random.randint(10000000, 99999999)}"
        }

    def test_register_and_apply(self):
        data = self.generate_random_data()
        self.open("https://mcitcareerssd.elevatus.io/")

        # Step 1: Register Candidate
        self.click("a[href='/register']")
        self.type("input[name='first_name']", data['first_name'])
        self.type("input[name='last_name']", data['last_name'])
        self.type("input[name='email']", data['email'])
        self.type("input[name='password']", data['password'])
        self.type("input[name='phone']", data['phone'])
        self.click("button[type='submit']")

        # Validation: Check registration success
        self.assert_text("Please check your email to activate your account", "div.alert-success")

        # Log in after registration (assuming auto-login is not enabled)
        self.type("input[name='email']", data['email'])
        self.type("input[name='password']", data['password'])
        self.click("button[type='submit']")

        # Validation: Check login success
        self.assert_element("a[href='/profile']")

        # Fill the profile manually
        self.click("a[href='/profile']")
        self.click("#fillProfileManually")

        # Validation: Check profile filling option
        self.assert_element("#fillProfileManually")

        # Navigate to Jobs and apply for the job
        self.click("a[href='/jobs']")
        self.click("button.apply-now-button")

        # Validation: Check job application success
        self.assert_text("Your application has been submitted", "div.alert-success")

        # Additional Validations
        self.assert_element("input[name='first_name']")
        self.assert_element("input[name='last_name']")
        self.assert_element("input[name='email']")
        self.assert_element("input[name='password']")
        self.assert_element("input[name='phone']")
        self.assert_element("a[href='/jobs']")
        self.assert_element("button.apply-now-button")

    def tearDown(self):
        self.save_screenshot_to_logs()
        super().tearDown()

if __name__ == "__main__":
    from seleniumbase import pytest
    pytest.main()

"""
import random
import string
from seleniumbase import BaseCase

class TestTask(BaseCase):

    def random_string(self, length=8):
        """ Generate a random string of fixed length """
        characters = string.ascii_lowercase + string.digits
        password = ''.join(random.choice(characters) for _ in range(length - 4))  # Adjust length to accommodate fixed characters
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        # Add one of each required character type to the password
        password += random.choice(string.ascii_uppercase)  # At least one uppercase letter
        password += random.choice(string.punctuation)      # At least one symbol
        password += random.choice(string.digits)           # At least one digit
        password += random.choice(string.ascii_lowercase)  # At least one lowercase letter
        return ''.join(random.sample(password, len(password)))  # Shuffle the password and return it

    def generate_email(self):
        """Generate a random email address ending with @gmail.com."""
        characters = string.ascii_lowercase + string.digits  # Ensure no symbols in email prefix
        prefix = ''.join(random.choice(characters) for _ in range(8))
        return f"{prefix}@gmail.com"

    def test_register_and_apply(self):
        self.open("https://mcitcareerssd.elevatus.io/")

        self.click("/html/body/div[3]/div/div[2]/div[1]/div[4]/button[1]")

        # Register Candidate
        self.click('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[5]/button[2]/span[1]')
        self.click('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[5]/button[2]/span[1]')

        # Fill in registration form with dynamic data
        first_name = self.random_string()
        last_name = self.random_string()
        email = self.generate_email()
        password = self.random_string(12)
        confirmation_password = password


        self.send_keys("input[placeholder='First name']", first_name)
        self.send_keys("input[placeholder='Last name']", last_name)
        self.send_keys("input[placeholder='Email']", email)
        self.send_keys("input[placeholder='Password']", password)
        self.send_keys("input[placeholder='Confirm Password']", confirmation_password)

        self.click("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[7]/label[1]")
        self.click("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[8]/button[1]")

        self.click('/html/body/div[1]/div/div/div/div[1]/div/form/div[8]/button')



if __name__ == "__main__":
    from seleniumbase.common import report
    report.main()
