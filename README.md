# ChallengeTwoAssign
This is the repository for challenge two

I am applying software-engineering best practices to add new features and enhancements to the loan qualifier application.

As a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet.

In the fileio.py file I added a function to read the csv, and save the csv.

In the same save csv function I wrote code to write the row and header. 

In the app.py file I added a questionary to return thee rate-sheet file by asking for the file path.

If the file path cannot be found, the code will prompt the user.

The questionary asks for the users credit score, debt, income, loan amount wished, and the value of the users home. 