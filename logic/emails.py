import logic.database as database


def send_email_to_host(uid):
    data = database.query_from_database(uid)
    h_email = data["host"]["h_email"]

    message = """
    Name - {}
    Email - {}
    Phone - {}
    CheckIn Time - {}
    CheckOut Time  - {}
    """.format(
        data["visitor"]["v_name"],
        data["visitor"]["v_email"],
        data["visitor"]["v_phone"],
        data["check_times"]["check_in"],
        data["check_times"]["check_out"],
    )

    # print(message)
    send_email(message, h_email)


def send_email_to_visitor(uid):
    data = database.query_from_database(uid)
    v_email = data["visitor"]["v_email"]

    message = """
    Name - {}
    Phone - {}
    CheckIn Time - {}
    CheckOut Time  - {}
    Host Name - {}
    Address Visited - {}
    """.format(
        data["visitor"]["v_name"],
        data["visitor"]["v_phone"],
        data["check_times"]["check_in"],
        data["check_times"]["check_out"],
        data["host"]["h_name"],
        data["host"]["address"],
    )

    # print(message)
    send_email(message, v_email)


def send_email(message, receiver_email_id=None):
    import os
    import smtplib
    from dotenv import load_dotenv

    load_dotenv()

    sender_email_id = os.getenv("SENDER_USERNAME")
    sender_password = os.getenv("SENDER_PASSWORD")
    if receiver_email_id == None:
        receiver_email_id = os.getenv("RECEIVER_EMAIL")

    with smtplib.SMTP("smtp.gmail.com", 587) as mail:
        mail.starttls()
        mail.login(sender_email_id, sender_password)

        mail.sendmail(sender_email_id, receiver_email_id, message)

        mail.quit()


if __name__ == "__main__":
    from datetime import datetime as dt

    send_email("\nHi There {}".format(dt.now()))
