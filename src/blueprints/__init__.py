from flask import Blueprint

from ..blueprints.tag import tag_bp

api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(tag_bp, url_prefix='/tag')
