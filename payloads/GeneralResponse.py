from typing import List

def payloads(status:str, results:int, data:list):
    return {
        "status_code":status,
        "results":results,
        "payloads":data
    }

def payload(status:str, results:int, data:list):
    return {
        "status_code":status,
        "results":results,
        "payloads":data
    }