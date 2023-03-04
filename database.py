from sqlalchemy import create_engine, text
import json
# Turn on database engine
engine = create_engine(f"sqlite:///jobscareer.db",
    #                    connect_args={
    #     "ssl": {
    #         "ca": "/home/gord/client-ssl/ca.pem",
    #         "cert": "/home/gord/client-ssl/client-cert.pem",
    #         "key": "/home/gord/client-ssl/client-key.pem"
    #     }
    # }
)

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        result_dict = []
        for row in result.all():
            """
            The results look like tuples/lists, but they are actually a special Row object 
            (KeyedTuple for SQLAlchemy < 1.4). Use the _asdict() method to convert each row 
            to a dict.
            """
            result_dict.append(row._asdict())
        return result_dict

def load_job(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id =:val"),
                              parameters={"val": id}
                              )
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()
        