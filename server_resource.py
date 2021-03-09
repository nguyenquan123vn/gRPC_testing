import json

import mssv_pb2


def read_database():
    sv_list = []
    with open("data.json") as info_sv_db_file:
        for item in json.load(info_sv_db_file):
            sv = mssv_pb2.infoSV(
                name=item["name"],
                id = mssv_pb2.idSV(mssv=item["Student_id"]),
                phone = item["phone"],
                address = item["address"],
                dateOfBirth = item["DOB"],
                age = item["age"],
                gender = item["gender"],
                mail = item["mail"]
            )
            sv_list.append(sv)
    return sv_list