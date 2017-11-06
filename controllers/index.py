from controllers.modules import *

class IndexHandler(RequestHandler):

    """
    class resposible to render the main page
    route : /
    """

    @coroutine
    def get(self):
        token = self.get_secure_cookie('token')

        if token:
            _id = untokenizeCokkie(token)
            isValidtkn = yield db.tokens.find_one({"token" : token, "_uid" : _id})
            if isValidtkn:
                data = yield db.users.find_one({"_id" : _id})
                if data:
                    self.redirect("/dashboard")
                else:
                    self.render("form.html")
        else:
            self.render("form.html")
