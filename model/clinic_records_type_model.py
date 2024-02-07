from pydantic import BaseModel


class ClinicRecordsType(BaseModel):
    value_clinic_records_type: str
