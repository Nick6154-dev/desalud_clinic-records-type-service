from typing import Optional, Annotated
from pydantic import BaseModel, BeforeValidator, Field

PyObjectId = Annotated[str, BeforeValidator(str)]


class ClinicRecordsType(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    value_clinic_records_type: str
