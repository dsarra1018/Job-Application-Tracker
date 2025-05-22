# Job Application Tracker

A simple command-line Python application to help you track your job applications, follow-ups, and interview progress - all from your terminal

## Features

- Add and save new job applications
- View all stored applications in a table
- Update application status (e.g. Applied -> Interviewing)
- Delete unwanted entries
- Search/filter by company or status
- Data stored locally using CSV for easy portability
- (Optional) Visual enhancements with colored terminal output

## Technologies Used

- Python
- `csv` module (for data storage)
- `datetime` (for date validation)
- `tabulate` (for table formatting)
- `colorama` (for colorful terminal output, optional)

## Folder Structure

```
job_application_tracker/
|--- main.py            # Main CLI logic
|--- storage.py         # Data saving/loading functions
|--- utils.py           # Input validation and helpers
|--- data.csv           # CSV file storing job applications
|--- README.md          # Project documentation
|--- requirements.txt   # Python dependencies
```

## Fields Tracked

Each application tracks the following:

- `Company Name`
- `Job Title`
- `Location`
- `Date Applied`
- `Status` (Applied, Interviewing, Rejected, Offer)
- `Contact Info`
- `Notes`

## Getting Started

1. **Clone the repo**
```bash
git clone https://github.com/dsarra1018/Job-Application-Tracker.git
cd Job-Application-Tracker
```

2. **Install dependencies**
*(Optional: for table formatting and colors)*
```bash
pip install -r requirements.txt
```

3. **Run the tracker**
```bash
python main.py
```

## Example Use

```bash
Welcome to the Job Application Tracker!
1. Add new application
2. View all applications
3. Update application status
4. Delete an application
5. Search applications
0. Exit
```

## Ideas for Future Features

- Add a GUI with Tkinter
- Send follow-up reminders via email
- Export filtered applications to PDF
- Web version with Flask or Django
- Application status analytics (charts with matplotlib)

## Contributing

Feel free to fork the project and submit PRs with improvements or new features!

## License

This project is open source and available under the [MIT License](LICENSE).