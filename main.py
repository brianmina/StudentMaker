# This is a sample Python script.
import requests
import segno


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def make_qr(qr_id, first_name, last_name, student_number):
    student_qr = segno.make_qr(qr_id)
    file_name = f"{first_name}_{last_name}_{student_number}.png"
    student_qr.save(
        file_name,
        border=2, scale=10, dark='#050d4f'
    )
    print(f"Qr code successfully created: {file_name}")


def main():
    active = True
    while active:
        first_name = input("Please enter the first name of the student:")
        last_name = input("Please enter the last name of the student:")
        student_number = input("Please enter the student number of the student:")
        period = input("Please enter the period of the student:")
        qr_id = create_student(first_name, last_name, student_number, period)
        if qr_id:
            make_qr(qr_id, first_name, last_name, student_number)
            is_continue = input("Continue? (Y/n)")
            active = is_continue != "n"
    print("Thank you.")


def create_student(first_name, last_name, student_number, period) -> int | None:
    url = "https://classroom-tracker-gu6t24lssq-uk.a.run.app/students"
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "student_number": student_number,
        "period": period,
    }

    response = requests.post(url, json=student)
    if response.status_code == 200:
        print("Student successfully created.")
        return response.json().get('id')
    else:
        print("Unable to create student.")
        print(response.text)
        print("Please try again.")
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
