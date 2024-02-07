from model.clinic_records_type_model import ClinicRecordsType
from config.dbConfig import initialize_mongo_instance
import os


async def get_collection(collection_name=None):
    if collection_name is None:
        collection_name = os.getenv('MONGO_DATABASE_COLLECTION', 'clinic_records_type')
    mongo = await initialize_mongo_instance()
    return mongo[collection_name]


async def find_all():
    collection = await get_collection()
    cursor = collection.find({}, {'_id': 0})
    documents = [doc async for doc in cursor]
    return documents


async def find_by_value_clinic_records_type(value_clinic_records_type: str):
    collection = await get_collection()
    filter_query = {'value_clinic_records_type': value_clinic_records_type}
    cursor = collection.find(filter_query, {'_id': 0})
    documents = [doc async for doc in cursor]
    return documents


async def save_new_clinic_records_type(clinic_records_type: ClinicRecordsType):
    collection = await get_collection()
    clinic_records_type_dict = clinic_records_type.dict()
    try:
        result = await collection.insert_one(clinic_records_type_dict)
        return result.inserted_id
    except Exception as e:
        return "Error al guardar el nuevo tipo de historia clinica: " + str(e)
