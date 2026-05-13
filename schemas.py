from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class PatientCreated(BaseModel):

    First_Name: str = Field(..., max_length=50)
    Middle_Name: Optional[str] = Field(default=None, max_length=50)
    Last_Name: str = Field(..., max_length=50)
    DOB: str
    Age: int
    Gender: str
    Phone: str = Field(..., min_length=10, max_length=15)
    Alternate_Phone: Optional[str] = Field(default=None, min_length=10, max_length=15)
    Email: EmailStr
    Blood_Group: str = Field(..., max_length=5)


class PatientUpdate(BaseModel):

    First_Name: Optional[str] = None
    Middle_Name: Optional[str] = None
    Last_Name: Optional[str] = None
    DOB: Optional[str] = None
    Age: Optional[int] = None
    Gender: Optional[str] = None
    Phone: Optional[str] = None
    Alternate_Phone: Optional[str] = None
    Email: Optional[EmailStr] = None
    Blood_Group: Optional[str] = None