import smtplib
from app.message import html_generation

EMAIL_SENDER = 'khamzin.adel22@gmail.com'
EMAIL_GETTER = 'xulkjldfbrccmwad'


def send(email_getter: str, gen_email_code: str):
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(EMAIL_SENDER, EMAIL_GETTER)
        smtp_server.sendmail(EMAIL_SENDER, email_getter, html_generation(gen_email_code, email_getter))
        smtp_server.quit()
    except smtplib.SMTPException:
        return 'Problems with gmail'
