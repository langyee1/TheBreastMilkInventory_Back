from app import db
from app.models.milk import Milk
from flask import Blueprint, jsonify, make_response, request, abort
from .routes_helpers import validate_model



milks_bp = Blueprint("milks", __name__, url_prefix="/milks")


@milks_bp.route("", methods=["POST"])
def add_new_milk():
    request_body = request.get_json()

    new_milk = Milk.dict_to_model(request_body)


    db.session.add(new_milk)
    db.session.commit()

    return make_response(f"Milk {new_milk.id} successfully created", 201)

@milks_bp.route("", methods=["GET"])
def get_all_milks():
    milks = Milk.query.all()
    milks_list=[milk.make_milk_dict()for milk in milks]

    return jsonify(milks_list), 200

@milks_bp.route("", methods=["DELETE"])
def delete_all_cards():
    milks = Milk.query.all()
    for milk in milks:
        db.session.delete(milk)
    db.session.commit()

    return make_response(jsonify("All milks successfully deleted!"), 200)

@milks_bp.route("/<milk_id>", methods=["GET"])
def get_one_milk(milk_id):

    milk = validate_model(Milk, milk_id)

    return milk.make_milk_dict(), 200


@milks_bp.route("/<milk_id>", methods=["DELETE"])
def delete_milk(milk_id):
    milk = validate_model(Milk, milk_id)

    db.session.delete(milk)
    db.session.commit()

    return make_response(f"Milk #{milk.id} successfully deleted")

@milks_bp.route("/<milk_id>", methods=["PUT"])
def update_milk(milk_id):
    milk=validate_model(Milk, milk_id)
    request_body=request.get_json()

    if request_body.get("amount") is None or request_body.get("container") is None or request_body.get("type") is None or request_body.get("cad") is None:
        return make_response(f"some additional information needed to update milk {milk.id}",400)

    milk.amount=request_body["amount"]
    milk.container=request_body["container"]
    milk.type=request_body["type"]
    milk.cad=request_body["cad"]

    db.session.commit()

    return make_response(f"milk {milk.id} succesfully updated",200)

