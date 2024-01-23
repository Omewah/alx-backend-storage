#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def nginx_stats_check():
    """provides some stats about Nginx logs"""
    cl = MongoClient()
    cl_logs = cl.logs.nginx

    cont_doc = cl_logs.count_documents({})
    print('{} logs'.format(cont_doc))

    list_method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in list_method:
        cont_method = cl_logs.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, cont_method))
    cont_stat = cl_logs.count_documents({
        "method": "GET", "path": "/status"
    })
    print('{} status check'.format(cont_stat))


if __name__ == "__main__":
    nginx_stats_check()
