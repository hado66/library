import hashlib
import uuid


def get_uuid():
    """
    生成UUID
    :return: UUID
    """
    uuid_str = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()
