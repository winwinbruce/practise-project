from my_app import db

class Employee(db.Document):
    key = db.IntField(unique=True, required=True)
    name = db.StringField(unique=True, required=True)
    age = db.IntField(reuired=True)
    birthDate = db.StringField()

    def json(self):
        employee_dic={
            "key":self.key,
            "name":self.username,
            "age":self.age,
            "birthDate":self.birthDate
                    }
        return json.dumps(employee_dic)
    
    def __repr__(self):
        return '<Employee %r>' % self.id