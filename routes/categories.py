from flask import Blueprint, jsonify

from services.CategoriesService import CategoriesService

route = Blueprint("categories", __name__)

categories_service = CategoriesService()


#########
###GET###
#########
@route.route('/', methods=['GET'])
def get_all_categories():
    try:
        all_categories = categories_service.get_all_categories()
        all_categories_json = []
        for cat in all_categories:
            all_categories_json.append(cat.convert_to_json())
        return all_categories_json
    except Exception as e:
        return jsonify({e.__class__.__name__: e.args[0]}), 500
