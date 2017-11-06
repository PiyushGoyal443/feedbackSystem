from controllers.modules import *

def tokenizeCokkie(_id):

    """
    function to tokenize cokkie and return it

    @params
    id : mongo user id
    """

    now = datetime.now()
    time = now.strftime("%d-%m-%Y %I:%M %p")

    token = jwt.encode({"id" : str(_id), "time" : time}, secret, algorithm = 'HS256')

    return token

def untokenizeCokkie(token):

    """
    function to untokenize cokkie and return payload from it

    @params
    token : tokenized_cokkie
    """

    payload = jwt.decode(token, verify = False)

    return ObjectId(payload["id"])
