from node.utils import instance_property
from cone.app.model import (
    BaseNode,
    ProtectedProperties,
    BaseMetadata,
)
from cone.app.security import DEFAULT_NODE_PROPERTY_PERMISSIONS


class S3(BaseNode):
    
    @instance_property
    def properties(self):
        props = ProtectedProperties(self, DEFAULT_NODE_PROPERTY_PERMISSIONS)
        props.in_navtree = True
        props.editable = False
        props.icon = 's3-static/images/s3_16_16.png'
        return props
    
    @instance_property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "S3"
        metadata.description = "S3 Storage connector for cone"
        return metadata