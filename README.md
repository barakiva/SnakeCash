# SnakeCash

A script I've made to make going over my credit card statements (I use Isracard) slightly less painful. 

The app takes in Isracard monthly reports. It cleans up redundant cells, provides proper column names in English (so you can upload it to an AI assistant and query it for financial questions) and produces two files: one csv for comfortable parsing, and one Excel file with each month as a separate sheet.

## Installation	

Clone the project, run pip install for the dependencies. Place all your monthly reports in the `reports` folder. Run the script using `python3 app.py` and you will get a nice excel sheet for browsing your credit card activites.

The app also prints monthly spend based on a set of vendors you provide under .env with USER_VENDORS. Obviously, this is private and user-specific so you'd have to create that .env yourself and populate it with the vendors you go to. I will try to make a more user friendly interface for that in the future.
