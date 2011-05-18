from cone.tile import registerTile
from cone.app.browser.layout import ProtectedContentTile
from cone.s3.model import S3

registerTile('content',
             'cone.s3:browser/templates/s3.pt',
             interface=S3,
             class_=ProtectedContentTile,
             permission='login')