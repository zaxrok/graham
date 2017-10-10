import pkg_resources


try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    # package is not installed
    pass


from graham.core import (
    create_metadata,
    dumps,
    register,
    schema,
    schemify,
)