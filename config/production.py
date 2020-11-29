from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b"\x8a\xe2&#\xfc\x04\xec\xfdj\xd4\xe6.\xd8'_\x17"