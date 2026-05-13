from fastapi import FastAPI
from database import SessionLocal
from models import Patient
from schemas import PatientCreated , PatientUpdate

app = FastAPI()


# GET ALL PATIENTS
@app.get("/patient")
def get_patient():

    db = SessionLocal()

    data = db.query(Patient).all()

    db.close()

    return data


# ADD PATIENT
@app.post("/patient")
def add_patient(patient: PatientCreated):

    db = SessionLocal()

    new_patient = Patient(
        First_Name=patient.First_Name,
        Middle_Name=patient.Middle_Name,
        Last_Name=patient.Last_Name,
        DOB=patient.DOB,
        Age=patient.Age,
        Gender=patient.Gender,
        Phone=patient.Phone,
        Alternate_Phone=patient.Alternate_Phone,
        Email=patient.Email,
        Blood_Group=patient.Blood_Group
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    db.close()

    return {
        "msg": "Patient Successfully Added"
    }


# UPDATE PATIENT
@app.put("/patient/{patient_id}")
def update_patient(patient_id: int, updated_data: PatientUpdate):

    db = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.Patient_id == patient_id
    ).first()

    if patient:

        if updated_data.First_Name is not None:
            patient.First_Name = updated_data.First_Name

        if updated_data.Middle_Name is not None:
            patient.Middle_Name = updated_data.Middle_Name

        if updated_data.Last_Name is not None:
            patient.Last_Name = updated_data.Last_Name

        if updated_data.DOB is not None:
            patient.DOB = updated_data.DOB

        if updated_data.Age is not None:
            patient.Age = updated_data.Age

        if updated_data.Gender is not None:
            patient.Gender = updated_data.Gender

        if updated_data.Phone is not None:
            patient.Phone = updated_data.Phone

        if updated_data.Alternate_Phone is not None:
            patient.Alternate_Phone = updated_data.Alternate_Phone

        if updated_data.Email is not None:
            patient.Email = updated_data.Email

        if updated_data.Blood_Group is not None:
            patient.Blood_Group = updated_data.Blood_Group

        db.commit()
        db.close()

        return {
            "msg": "Patient updated successfully"
        }

    db.close()

    return {
        "msg": "Patient not found"
    }


@app.patch("/patient/{patient_id}")
def patch_patient(
        patient_id: int,
        phone: str = None,
        email: str = None
):

    db = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.Patient_id == patient_id
    ).first()

    if patient:

        if phone:
            patient.Phone = phone

        if email:
            patient.Email = email

        db.commit()

        db.close()

        return {
            "msg": "Patient partially updated"
        }

    db.close()

    return {
        "msg": "Patient not found"
    }

# DELETE PATIENT
@app.delete("/patient/{patient_id}")
def remove_patient(patient_id: int):

    db = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.Patient_id == patient_id
    ).first()

    if patient:

        db.delete(patient)
        db.commit()

        db.close()

        return {
            "msg": "Patient successfully deleted"
        }

    db.close()

    return {
        "msg": "Patient not found"
    }


