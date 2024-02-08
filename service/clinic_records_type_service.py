from typing import List
from model.clinic_records_type_model import ClinicRecordsType
from config.dbConfig import initialize_mongo_instance
import os


async def get_collection(collection_name=None):
    if collection_name is None:
        collection_name = os.getenv('MONGO_DATABASE_COLLECTION', 'clinic_records_type')
    mongo = await initialize_mongo_instance()
    return mongo[collection_name]


async def find_all() -> List[ClinicRecordsType]:
    collection = await get_collection()
    cursor = collection.find()
    documents = await cursor.to_list(length=None)
    clinic_records_types = [ClinicRecordsType.parse_obj(doc) for doc in documents]
    return clinic_records_types


async def find_by_value_clinic_records_type(value_clinic_records_type: str) -> ClinicRecordsType | None:
    collection = await get_collection()
    filter_query = {'value_clinic_records_type': value_clinic_records_type}
    document = await collection.find_one(filter_query)
    if document:
        clinic_records_type = ClinicRecordsType.parse_obj(document)
        return clinic_records_type
    else:
        return None


async def save_new_clinic_records_type(clinic_records_type: ClinicRecordsType) -> str:
    already_saved = await find_by_value_clinic_records_type(clinic_records_type.value_clinic_records_type)
    if already_saved:
        return "Clinic records type already saved"
    collection = await get_collection()
    clinic_records_type_dict = clinic_records_type.dict()
    try:
        await collection.insert_one(clinic_records_type_dict)
        return "Clinic records type saved successfully"
    except Exception as e:
        return "Error al guardar el nuevo tipo de historia clinica: " + str(e)
