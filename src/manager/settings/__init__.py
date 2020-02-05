from .base import *

try:
    from .local import *
except Exception as e:
    from .production import *

# # for testing only
# try:
#     from .local import *
#     print('>>> Loaded local settings')
# except Exception as e:
#     print('>>> Error in local settings:', e)
#     from .production import *
#     print('>>> Loaded production settings')
