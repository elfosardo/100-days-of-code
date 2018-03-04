import argparse
import config as cfg
import email.utils
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def generate_arguments():
    parser = argparse.ArgumentParser(description='Simple mail sender client')
    parser.add_argument('sender',
                        help='email address of the sender')
    parser.add_argument('recipient',
                        help='email address of the receiver')
    parser.add_argument('--subject', '-s', dest='subject', type=str,
                        help='subject of the email')
    parser.add_argument('--debug', '-d', dest='debug', action='store_true',
                        help='debug mode')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--message', '-m', dest='message', type=str,
                       help='message to send')
    group.add_argument('--file', '-f', dest='msg_file',
                       help='file with text to send')
    arguments = parser.parse_args()
    return arguments


def compose_message():
    msg = ''
    if args.message is not None:
        msg = MIMEText(args.message)
    elif args.msg_file is not None:
        with open(args.msg_file) as msg_file:
            msg = MIMEMultipart()
            body = msg_file.read()
            msg.attach(MIMEText(body, 'plain'))
    msg['To'] = email.utils.formataddr(('Recipient', args.recipient))
    msg['From'] = email.utils.formataddr(('Sender', args.sender))
    msg['Subject'] = args.subject
    return msg.as_string()


if __name__ == '__main__':
    args = generate_arguments()

    my_message = compose_message()

    smtp_server = smtplib.SMTP(cfg.SMTP_SERVER, cfg.SMTP_PORT)
    if args.debug:
        smtp_server.set_debuglevel(True)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(args.sender, cfg.gmail_app_pw)

    smtp_server.sendmail(args.sender, [args.recipient], my_message)

    smtp_server.quit()

    print('Email sent!')
