import os
import json


users_cvs_route_str = "./users.json"

def fn_read_json(route_str):
    data_list = []

    if not os.path.exists(route_str):
        return data_list

    with open(route_str, "r", encoding="utf-8") as f:
        data_list = json.load(f)

    return data_list


def fn_write_json(route_str, data_list):
    with open(route_str, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)

def fn_create_cv():
    name_str = input("type your name: ")
    last_names_str = input("type your last name: ")
    birth_date_str = input("type your birth date (date format): ")
    tecnologies_list = input("type all the technologies you know: ").split(",")
    experience_int = int(input("type your experience: "))
    additional_information_str = input("type additional information: ")
    career_str = input("type your career: ")
    languages_list = input("type your languages with commas: ").split(",")
    phone_number_str = input("type your phone number: ")

    email_str = input("type your email: ")

    while "@" not in email_str or "." not in email_str.split("@")[-1] or " " in email_str:
        print("Please enter a valid email")
        email_str = input("type your email: ")

    cv_info_dict = {
        "id": int(time.time() * 1000),
        "name": name_str,
        "last_names": last_names_str,
        "birth_date": birth_date_str,
        "tecnologies": tecnologies_list,
        "experience": experience_int,
        "additional_information": additional_information_str,
        "career": career_str,
        "languages": languages_list,
        "phone_number": phone_number_str,
        "email": email_str
    }

    return cv_info_dict


def fn_edit_cv(data_dict):
    cv_inputs_list = [
        "name", "last_names", "birth_date", "tecnologies",
        "experience", "additional_information", "career",
        "languages", "phone_number", "email"
    ]

    print(cv_inputs_list)

    wants_to_answer_list = input("Fields to edit (comma separated): ").split(",")

    for field_str in wants_to_answer_list:
        field_str = field_str.strip()

        if field_str in cv_inputs_list:

            if field_str == "experience":
                data_dict[field_str] = int(input(field_str + ": "))

            elif field_str == "tecnologies" or field_str == "languages":
                data_dict[field_str] = input(field_str + ": ").split(",")

            elif field_str == "email":
                email_str = input("email: ")

                while "@" not in email_str or "." not in email_str.split("@")[-1] or " " in email_str:
                    print("Please enter a valid email")
                    email_str = input("email: ")

                data_dict[field_str] = email_str

            else:
                data_dict[field_str] = input(field_str + ": ")

    return data_dict

    def fn_edit_cv(data_dict):
    cv_inputs_list = [
        "name", "last_names", "birth_date", "tecnologies",
        "experience", "additional_information", "career",
        "languages", "phone_number", "email"
    ]


    print(cv_inputs_list)


    wants_to_answer_list = input("Fields to edit (comma separated): ").split(",")


    for field_str in wants_to_answer_list:
        field_str = field_str.strip()


        if field_str in cv_inputs_list:


            if field_str == "experience":
                data_dict[field_str] = int(input(field_str + ": "))


            elif field_str == "tecnologies" or field_str == "languages":
                data_dict[field_str] = input(field_str + ": ").split(",")


            elif field_str == "email":
                email_str = input("email: ")


                while "@" not in email_str or "." not in email_str.split("@")[-1] or " " in email_str:
                    print("Please enter a valid email")
                    email_str = input("email: ")


                data_dict[field_str] = email_str


            else:
                data_dict[field_str] = input(field_str + ": ")


    return data_dict


