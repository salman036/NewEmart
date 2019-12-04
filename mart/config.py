class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///emart.db'
    SECRET_KEY = '123456789'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'salmansaleem036@gmail.com '
    MAIL_PASSWORD = '@pakianon33@321'

    broker_url = 'pyamqp://'
    result_backend = 'rpc://'

    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timezone = 'Europe/Oslo'
    enable_utc = True
