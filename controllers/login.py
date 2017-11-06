from controllers.modules import *

class LoginHandler(RequestHandler):

    @coroutine
    def get(self):

        uname = self.get_argument("uname")
        pswd = self.get_argument("pswd")

        data = yield db.users.find_one({"uname" : uname, "pswd" : pswd})

        if res:
            token = tokenizeCokkie(data["_id"])
            self.set_secure_cookie('token', token)

            temp = yield db.tokens.insert({"_uid" : data["_id"],
									"time" : today,
									"token" : token})
            self.redirect("/dashboard")
        else:
            self.redirect("/?credentials=False")
