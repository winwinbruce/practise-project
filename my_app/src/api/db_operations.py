
from flask import request, jsonify, Blueprint
from my_app.src.db.model import Employee
from my_app.src.db.logging import logger
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

db_operations = Blueprint('db_operations', __name__)


@db_operations.route("/employee", methods=['POST',])
def add_one():
    content = request.get_json()
    employee = Employee(
        key=content["key"],
        name=content["name"],
        age=content['age'],
        birthDate=content['birthDate']
    ).save()
    return {"status":"create success"}


@db_operations.route("/find", methods=['GET',])
def employee():
    employee = Employee.objects.first()
    res ={}
    res["employee"+str(employee.key)] = {"name":employee.name, "age":employee.age, "birth":employee.birthDate}
    return jsonify(res)

@db_operations.route("/findAll", methods=['GET',])
def employees():
    employees = Employee.objects.all()
    res = {}
    for employee in employees:
        res["employee"+str(employee.key)] = {"name":employee.name, "age":employee.age, "birth":employee.birthDate}
    return jsonify(res)

@db_operations.route("/delete", methods=['POST',])
def delete():
    Employee.objects.first().delete()
    return {"status":"delete success"}

@db_operations.route("/update", methods=['POST',])
def update():
    content = request.get_json()
    Employee.objects.filter(key=content['key']).first().update(age=content['age'])
    return {"status":"update success"}

@db_operations.route("/healthCheck", methods=['GET'])
def check_db_connection():
    try:
        client = MongoClient(serverSelectionTimeoutMS = 2000)
        client.admin.command('ismaster')
        logger.info('DB connect success')
        return {"status":"DB connect success"}
    except ConnectionFailure:
        logger.error("DB connect failed")
        return {"status":"DB connect failed"}


   
    

