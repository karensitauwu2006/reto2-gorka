import os
import json


users_cvs_route_str = "./users.json"

def fn_read_json(route_str): # funcion para leer json
    data_list = []

    if not os.path.exists(route_str): # para asegurarse que existe el archivo, sin o existe devuelve una lista vacia
        return data_list 

    with open(route_str, "r", encoding="utf-8") as f:
        data_list = json.load(f)

    return data_list


def fn_write_json(route_str, data_list): # funcion para leer 
    with open(route_str, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False) # esto escribe en el archivo mediante la fucnion dump de json

def fn_create_cv(): # funcion para crear cv, pregunta por todos los datos y hace un dict
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


def fn_edit_cv(data_dict): # funcion para ecitar un cv existente 
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


def fn_format_cv(cv_dict):
    print("\n" + "=" * 40)
    print("             CURRICULUM VITAE")
    print("=" * 40)


    print(f"\nID: {cv_dict['id']}")


    print("\nPERSONAL INFORMATION")
    print("-" * 40)
    print(f"Name: {cv_dict['name']} {cv_dict['last_names']}")
    print(f"Birth date: {cv_dict['birth_date']}")
    print(f"Phone: {cv_dict['phone_number']}")
    print(f"Email: {cv_dict['email']}")


    print("\nPROFESSIONAL INFORMATION")
    print("-" * 40)
    print(f"Career: {cv_dict['career']}")
    print(f"Experience: {cv_dict['experience']} years")


    print("\nTECHNOLOGIES")
    print("-" * 40)
    for technology_str in cv_dict["tecnologies"]:
        print(f"- {technology_str.strip()}")


    print("\nLANGUAGES")
    print("-" * 40)
    for language_str in cv_dict["languages"]:
        print(f"- {language_str.strip()}")


    print("\nADDITIONAL INFORMATION")
    print("-" * 40)
    print(cv_dict["additional_information"])


    print("\n" + "=" * 40)

def fn_search_cv(data_list):
    if not data_list:
        print("There are no CVs registered")
        return None


    for cv_dict in data_list:
        print(f"ID: {cv_dict['id']} | Name: {cv_dict['name']} {cv_dict['last_names']}")


    cv_id_int = int(input("\nType the CV ID: "))


    for cv_dict in data_list:
        if cv_dict["id"] == cv_id_int:
            return cv_dict


    print("CV not found")
    return None

def main():
    print("welcome to your CV/json creator")


    while True:
        print("\nchoose an option")
        print("create a new CV - 1")
        print("edit existing CV - 2")
        print("view your own CV - 3")
        print("visualize all CVs - 4")
        print("exit - 0")


        user_input_int = int(input("type your input: "))


        if user_input_int == 0:
            break


        elif user_input_int == 1:
            created_data_dict = fn_create_cv()
            read_data_list = fn_read_json(users_cvs_route_str)
            read_data_list.append(created_data_dict)
            fn_write_json(users_cvs_route_str, read_data_list)
            print("CV created successfully")


        elif user_input_int == 2:
            read_data_list = fn_read_json(users_cvs_route_str)
            cv_dict = fn_search_cv(read_data_list)


            if cv_dict:
                fn_edit_cv(cv_dict)
                fn_write_json(users_cvs_route_str, read_data_list)
                print("CV updated successfully")


        elif user_input_int == 3:
            read_data_list = fn_read_json(users_cvs_route_str)
            cv_dict = fn_search_cv(read_data_list)


            if cv_dict:
                fn_format_cv(cv_dict)
                input()


        elif user_input_int == 4:
            read_data_list = fn_read_json(users_cvs_route_str)


            for cv_dict in read_data_list:
                fn_format_cv(cv_dict)


            input()


        else:
            print("Invalid option")




main()


