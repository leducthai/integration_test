import yaml
import logging
import os
import re

from connections import mariadb
from caller import Caller
from assert_call import StatusCodeAssertion
import logger
import flagging
import steps.test_load_feature as test_load_feature
_logger = logging.getLogger(__name__)

# with open("config.yaml", "br") as conf:
#     data = yaml.safe_load(conf)
#     mariadb_conn = data.get("mariadb_connection")
#     _logger.info("connecting to DB")

#     db_conn = mariadb.DbConnection(
#         db_host=mariadb_conn.get("db_host"),
#         db_port=mariadb_conn.get("db_port"),
#         db_name=mariadb_conn.get("db_name"),
#         db_user=mariadb_conn.get("db_user"),
#         db_password=mariadb_conn.get("db_password")
#     )


# _root_path = "./data_test"
# file_pattern = re.compile(r'.*.ya?ml$', re.IGNORECASE)
# composers = []

# for root, _, files in os.walk(_root_path):
#     for file in files:
#         if re.match(file_pattern, file):
#             new_com = TestCaseComposer(filename=root + "/" + file)   
#             composers.append(new_com)
            


# for com in composers:
#     callers = []
    
#     for co in com.get_arrange_calls():
#         callers.append(Caller(co))
#         status_list = com.get_status_codes()
        
#     # arrange
#     while callers:
#         callers.pop(0)()
    
#     # action
#     for co in com.get_action_calls():
#         callers.append(Caller(co))
    
        
#     actions = StatusCodeAssertion(api_calls=callers, status=com.get_status_codes())
#     actions()
    

