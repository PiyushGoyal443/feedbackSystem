from controllers.modules import *

class FeedbackHandler(RequestHandler):

    def post(self):
        token = self.get_secure_cookie('token')

        if token:
            _id = untokenizeCokkie(token)
            isValidtkn = yield db.tokens.find_one({"token" : token, "_uid" : _id})

            if isValidtkn:
                data = yield db.users.find_one({"_id" : _id})
                if data:
                    course_id = self.get_argument("course_id")
                    fdbk = {
                        "q1" : self.get_argument("q1"),
                        "q2" : self.get_argument("q2"),
                        "q3" : self.get_argument("q3"),
                        "q4" : self.get_argument("q4"),
                        "q5" : self.get_argument("q5")
                    }

                    yield db.feedback.insert_one({"course_id" : course_id, "uid" : _id, "feedback" : fdbk})
                else:
                    self.redirect("/?user=invalid")
            else:
                self.redirect("/?token=False")
        else:
            self.redirect("/?loggedin=False")
