from fastapi import APIRouter
from service import clinic_records_type_service
from model.clinic_records_type_model import ClinicRecordsType
from fastapi import HTTPException
from fastapi.param_functions import Body

router = APIRouter(prefix="/clinicRecordsTypeService", tags=["clinicRecordsType"])


@router.get("/findAll")
async def find_all():
    return await clinic_records_type_service.find_all()


@router.get("/findByClinicRecordsType/{value_clinic_records_type}")
async def find_by_clinic_records_type(value_clinic_records_type: str):
    return await clinic_records_type_service.find_by_value_clinic_records_type(value_clinic_records_type)


@router.post("/saveNewClinicRecordsType")
async def save_new_clinic_records_type(clinic_records_type: ClinicRecordsType = Body(...)):
    if clinic_records_type is None:
        raise HTTPException(status_code=400, detail="ClinicRecordType object is required")
    result = await clinic_records_type_service.save_new_clinic_records_type(clinic_records_type)
    return {"message": "Role saved successfully", "inserted_id": str(result)}

