def payloads(results:str, data:list):
    return {
        "messages":results,
        "payloads":data
    }

def payload(results:str, data:list):
    return {
        "messages":results,
        "payloads":data
    }

def logging(data:list):
    return{
        "payloads":data
    }