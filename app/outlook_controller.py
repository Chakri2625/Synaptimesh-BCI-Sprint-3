from app.enhanced_logger import log_command
import os
import time
import pyautogui


def open_outlook():

    log_command(
        "[EXECUTING] OPEN_OUTLOOK"
    )

    os.system(
        "start outlook"
    )

    time.sleep(2)

    log_command(
        "[SUCCESS] OUTLOOK_OPENED"
    )


def create_new_mail():

    log_command(
        "[EXECUTING] CREATE_NEW_MAIL"
    )

    pyautogui.hotkey(
        "ctrl",
        "n"
    )

    time.sleep(2)

    log_command(
        "[SUCCESS] NEW_MAIL_OPENED"
    )


def navigate_to_subject():

    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.press("tab")

    time.sleep(0.5)


def write_email(

    subject,

    body

):

    navigate_to_subject()

    pyautogui.write(
        subject,
        interval=0.03
    )

    time.sleep(1)

    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.write(
        body,
        interval=0.01
    )

    time.sleep(1)


def save_draft():

    log_command(
        "[EXECUTING] SAVE_DRAFT"
    )

    pyautogui.hotkey(
        "ctrl",
        "s"
    )

    time.sleep(2)

    log_command(
        "[SUCCESS] DRAFT_SAVED"
    )


def close_draft():

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    time.sleep(2)


def close_outlook():

    log_command(
        "[EXECUTING] CLOSE_OUTLOOK"
    )

    os.system(
        "taskkill /F /IM outlook.exe"
    )

    time.sleep(2)

    log_command(
        "[SUCCESS] OUTLOOK_CLOSED"
    )


def run_sick_leave_workflow():

    log_command(
        "=== STARTING SICK LEAVE WORKFLOW ==="
    )

    create_new_mail()

    write_email(

        "Sick Leave Request",

        """Dear Sir,

I am feeling unwell and unable to attend work today.

Kindly grant me sick leave for today.

Thank you.

Regards,
Chakradhar Kadali"""
    )

    save_draft()

    close_draft()

    log_command(
        "=== SICK LEAVE WORKFLOW COMPLETE ==="
    )


def run_promotion_request_workflow():

    log_command(
        "=== STARTING PROMOTION REQUEST WORKFLOW ==="
    )

    create_new_mail()

    write_email(

        "Promotion Request",

        """Dear Sir,

I would like to formally request consideration for promotion based on my performance and contributions.

I would be grateful for an opportunity to discuss this further.

Thank you.

Regards,
Chakradhar Kadali"""
    )

    save_draft()

    close_draft()

    log_command(
        "=== PROMOTION REQUEST WORKFLOW COMPLETE ==="
    )


def run_leave_application_workflow():

    log_command(
        "=== STARTING LEAVE APPLICATION WORKFLOW ==="
    )

    create_new_mail()

    write_email(

        "Leave Application",

        """Dear Sir,

I would like to apply for leave due to personal reasons.

Kindly approve my leave request.

Thank you.

Regards,
Chakradhar Kadali"""
    )

    save_draft()

    close_draft()

    log_command(
        "=== LEAVE APPLICATION WORKFLOW COMPLETE ==="
    )


def run_outlook_workflow():

    log_command(
        "=== STARTING OUTLOOK AUTOMATION ==="
    )

    open_outlook()

    run_sick_leave_workflow()

    time.sleep(1)

    run_promotion_request_workflow()

    time.sleep(1)

    run_leave_application_workflow()

    time.sleep(1)

    close_outlook()

    log_command(
        "=== OUTLOOK AUTOMATION COMPLETE ==="
    )