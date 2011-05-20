from plumber import (
    plumber,
    default,
    extend,
    Part,
)
from node.parts import (
    NodeChildValidate,
    Adopt,
    Order,
    AsAttrAccess,
    Nodify,
)
#from node.utils import instance_property
from boto.s3.connection import (
    S3Connection,
    OrdinaryCallingFormat,
)
from boto.s3.key import Key


def s3_root(node):
    while node and not isinstance(node, S3EntryNode):
        node = node.__parent__
    return node


class S3Config(object):
    
    def __init__(self):
        self.user = 'tester'
        self.password = 'testpw'
        self.host = 'localhost'
        self.port = 8091
        self.path = '/'
        self.calling_format = OrdinaryCallingFormat()
        self.is_secure = False


class S3Entry(Part):
    
    @default
    @property
    def conn(self):
        conf = self.config
        conn = S3Connection(aws_access_key_id=conf.user,
                            aws_secret_access_key=conf.password,
                            port=conf.port, 
                            calling_format=conf.calling_format,
                            host="localhost",
                            path=conf.path,
                            is_secure=conf.is_secure)
        return conn
    
    @extend
    def __getitem__(self, key):
        raw = self.conn.lookup(key)
        if not raw:
            raise KeyError(key)
        return S3BucketNode(key, self, raw)
    
    @extend
    def __setitem__(self, key, value):
        if not isinstance(value, S3BucketNode):
            raise ValueError(value)
        # XXX: hangs if inexistent instead of error ???
        self.conn.create_bucket(key)
    
    @extend
    def __delitem__(self, key):
        self.conn.delete_bucket(self.conn.get_bucket(key))
    
    @extend
    def __iter__(self):
        res = self.conn.get_all_buckets()
        for bucket in res:
            yield bucket.name


class S3EntryNode(object):
    __metaclass__ = plumber
    __plumbing__ = (
        NodeChildValidate,
        Adopt,
        Order,
        AsAttrAccess,
        Nodify,
        S3Entry,
    )
    
    def __init__(self, name=None, parent=None, config=None):
        self.__name__ = name
        self.__parent__ = parent
        self.config = config


class S3Bucket(Part):
    
    @extend
    def __getitem__(self, key):
        pass
    
    @extend
    def __setitem__(self, key, value):
        pass
    
    @extend
    def __delitem__(self, key):
        pass
    
    @extend
    def __iter__(self):
        pass


class S3BucketNode(object):
    __metaclass__ = plumber
    __plumbing__ = (
        NodeChildValidate,
        Adopt,
        Order,
        AsAttrAccess,
        Nodify,
        S3Bucket,
    )
    
    def __init__(self, name=None, parent=None, bucket=None):
        self.__name__ = name
        self.__parent__ = parent
        self.bucket = bucket


class S3Key(Part):
    
    @extend
    def __getitem__(self):
        pass
    
    @extend
    def __setitem__(self):
        pass
    
    @extend
    def __delitem__(self):
        pass
    
    @extend
    def __iter__(self):
        pass
