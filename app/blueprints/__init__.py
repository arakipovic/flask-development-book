from flask import Blueprint

blueprint = Blueprint('app_bp', __name__, template_folder='..templates')

from views import (index_with_session_and_post_redirect, index, route_with_cookie, redirect_example, abort)
