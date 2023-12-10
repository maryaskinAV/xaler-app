from uuid import uuid4


def upload_image(instance, filename) -> str:
    """

    :param instance:
    :param filename:
    :return:
    """
    ext = filename.split(".")[-1]

    if instance.__class__.__name__ == "User":
        new_filename = f"{uuid4()}.{ext}"
        return f"{instance.__class__.__name__.lower()}/{instance.id}/{instance.id}/{new_filename}"

    new_filename = f"%YYYY-%mm-%dd.{ext}"

    return f"{instance.__class__.__name__.lower()}/{new_filename}"
