# Automation-Python-


# Careerportal Test Automation

This repository contains a Python test script using SeleniumBase to automate the following tasks on the MCIT Careers website:
1. Register a new candidate
2. Apply for a job

## Usage

### Prerequisites
1. Python 3.x installed on your machine
2. Install SeleniumBase:
    ```bash
    pip install seleniumbase
    ```

### Running the Tests

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/mcit-careers-automation.git
    cd mcit-careers-automation
    ```

2. **Run the test script:**
    ```bash
    pytest --html=report.html --self-contained-html
    ```

This command will execute the test script and generate an HTML report (`report.html`) with the test results.

### Test Description

The test script performs the following steps:
1. Opens the MCIT Careers website
2. Registers a new candidate with dynamically generated data
3. Selects the "Fill the profile manually" option
###pending
4. Applies for a job
5. Validates registration and application success
6. Performs additional data validations

### Dynamic Data Generation

The script dynamically generates the following data for each run:
- First name
- Last name
- Email address
- Password (contains at least one uppercase letter, one symbol, one digit, and one lowercase letter)

### Contact

If you have any questions or need further assistance, please feel free to contact me at [m.ashraf@elevatus.com].

