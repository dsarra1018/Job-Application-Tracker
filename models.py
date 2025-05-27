from dataclasses import dataclass

@dataclass
class JobApplication:
    Company_Name: str
    Job_Title: str
    Location: str
    Date_Applied: str
    Status: str
    Contact_Info: str
    Notes: str