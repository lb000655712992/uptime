from database.config import session
from database.config import data_table, eMail, config_table
from database.config import data_tableSchema, eMailSchema, config_tableSchema


class config_table_backend:
    def create(frontend_data):
        try:
            # print(frontend_data)
            instance = config_table(frontend_data)
            session.add(instance)
            session.commit()
            session.close()
            return frontend_data
        except Exception as e:
            return e
            
    def read(ID=None):
        try:
            if ID:
                select_result = session.query(config_table).filter(config_table.ID == ID).all()
                count = session.query(config_table).filter(config_table.ID == ID).count()
            else:
                select_result = session.query(config_table).all()
                count = session.query(config_table).count()
            # print(select_result)
            if count:
                config_table_schema = config_tableSchema()
                return_data = []
                for i in range(count):
                    return_data.append(config_table_schema.dump(select_result[i]))
                session.close()
                return return_data
            else:
                return []
        except Exception as e:
            return e

    def update(frontend_data):
        try:
            config_table_schema = config_tableSchema()
            select_result = session.query(config_table).filter(config_table.ID == frontend_data.get("ID")).first()
            load_data = config_table_schema.load(frontend_data, session=session)
            select_result = load_data
            session.commit()
            select_result1 = session.query(config_table).filter(config_table.ID == frontend_data.get("ID")).first()
            return_data = config_table_schema.dump(select_result1)
            session.close()
            return return_data
        except Exception as e:
            return e

    def delete(frontend_data):
        try:
            session.query(config_table).filter(
                config_table.ID == frontend_data.get("ID")
            ).delete()
            session.commit()
            session.close()
            return "success"
        except Exception as e:
            return e

    def get_count():
        count = session.query(config_table).count()
        session.close()
        return count


class data_table_backend:
    def create(frontend_data):
        try:
            #print(frontend_data)
            instance = data_table(frontend_data)
            session.add(instance)
            session.commit()
            session.close()
            return frontend_data
        except Exception as e:
            return e
            
    def read(ID=None):
        try:
            if ID:
                select_result = session.query(data_table).filter(data_table.ID == ID).all()
                count = session.query(data_table).filter(data_table.ID == ID).count()
            else:
                select_result = session.query(data_table).all()
                count = session.query(data_table).count()
            # print(select_result)
            if count:
                data_table_schema = data_tableSchema()
                return_data = []
                for i in range(count):
                    return_data.append(data_table_schema.dump(select_result[i]))
                session.close()
                return return_data
            else:
                return []
        except Exception as e:
            return e

    def update(frontend_data):
        try:
            data_table_schema = data_tableSchema()
            select_result = session.query(data_table).filter(data_table.ID == frontend_data.get("ID")).first()
            load_data = data_table_schema.load(frontend_data, session=session)
            select_result = load_data
            session.commit()
            select_result1 = session.query(data_table).filter(data_table.ID == frontend_data.get("ID")).first()
            return_data = data_table_schema.dump(select_result1)
            session.close()
            return return_data
        except Exception as e:
            return e

    def delete(frontend_data):
        try:
            session.query(data_table).filter(
                data_table.ID == frontend_data.get("ID")
            ).delete()
            session.commit()
            session.close()
            return "success"
        except Exception as e:
            return e

    def get_count():
        return session.query(data_table).count()


class eMail_backend:
    def create(frontend_data):
        try:
            instance = eMail(frontend_data)
            session.add(instance)
            session.commit()
            return frontend_data
        except Exception as e:
            return e
            
    def read(ID=None):
        try:
            if ID:
                select_result = session.query(eMail).filter(eMail.ID == ID).all()
                count = session.query(eMail).filter(eMail.ID == ID).count()
            else:
                select_result = session.query(eMail).all()
                count = session.query(eMail).count()
            print(select_result)
            if count:
                eMail_schema = eMailSchema()
                return_data = []
                for i in range(count):
                    return_data.append(eMail_schema.dump(select_result[i]))
                return return_data
            else:
                return []
        except Exception as e:
            return e

    def update(frontend_data):
        try:
            eMail_schema = eMailSchema()
            select_result = session.query(eMail).filter(eMail.ID == frontend_data.get("ID")).first()
            load_data = eMail_schema.load(frontend_data, session=session)
            select_result = load_data
            session.commit()
            select_result1 = session.query(eMail).filter(eMail.ID == frontend_data.get("ID")).first()
            return_data = eMail_schema.dump(select_result1)
            return return_data
        except Exception as e:
            return e

    def delete(frontend_data):
        try:
            session.query(eMail).filter(
                eMail.ID == frontend_data.get("ID")
            ).delete()
            session.commit()
            return "success"
        except Exception as e:
            return e
    
    def get_count():
        return session.query(eMail).count()
