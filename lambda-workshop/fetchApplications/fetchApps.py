import json
import json
import psycopg2
import logging
import os
import sys
import boto3

# import requests
# rds settings
rds_host  = os.environ.get('RDS_HOST')
rds_username = os.environ.get('RDS_USERNAME')
rds_user_pwd = os.environ.get('RDS_USER_PWD')
rds_db_name = os.environ.get('RDS_DB_NAME')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
                    (rds_host, rds_username, rds_user_pwd, rds_db_name)
    conn = psycopg2.connect(conn_string)
except:
    logger.error("ERROR: Could not connect to Postgres instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS Postgres instance succeeded")

def lambda_handler(event, context):
    cur = conn.cursor();
    cur.execute("SELECT * FROM application_requests");
    rows = cur.fetchall();
    #list of string to store results
    results = []
    for row in rows:
        results.append(row);
    
    #results to string
    
    cur.close();      
   
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": str(results),
            # "location": ip.text.replace("\n", "")
        }),
    }

