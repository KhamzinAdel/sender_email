from email.mime.text import MIMEText


def html_generation(gen_email_code: str, email_getter: str) -> str:
    try:
        with open('app/templates/mess.html', encoding='utf-8') as file:
            template = file.read()
            message = template.replace('[gen_form]', gen_email_code).replace('[gen_email]', email_getter)
    except IOError:
        return 'The template file doesnt found'

    msg = MIMEText(message, 'html', _charset='utf-8')
    msg['Subject'] = 'Код подтверждения КФУ'

    return msg.as_string()
