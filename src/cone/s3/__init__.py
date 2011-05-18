import cone.app
from cone.s3.model import S3

cone.app.cfg.css.protected.append('s3-static/styles.css')

cone.app.register_plugin('s3', S3)