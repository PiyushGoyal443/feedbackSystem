from controllers.modules import *

class DashboardHandler(RequestHandler):

    @coroutine
    def get(self):

        token = self.get_secure_cookie('token')

        if token:
            _id = untokenizeCokkie(token)
            isValidtkn = yield db.tokens.find_one({"token" : token, "_uid" : _id})

            if isValidtkn:
                data = yield db.users.find_one({"_id" : _id})
                if data:
                    sub = []
                    for i in data["courses"]:
                        temp = yield db.courses.find_one({"_id" : i})
                        sub.append(temp)

                    self.render("dashboard.html", data = data, courses = sub)
                else:
                    self.redirect("/?user=invalid")
            else:
                self.redirect("/?token=False")
        else:
            self.redirect("/?loggedin=False")
