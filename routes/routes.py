"""
module to storing all the routes
"""

from controllers import *

routes = [
    (
        r"/",
        index.IndexHandler
    ),
    (
        r"/login",
        login.LoginHandler
    ),
    (
        r"/dashboard",
        dashboard.DashboardHandler
    ),
    (
        r"/feedback",
        feedback.FeedbackHandler
    )
]
