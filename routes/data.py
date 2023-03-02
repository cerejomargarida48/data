from flask import abort, Blueprint
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.annotations import doc
from marshmallow import fields

from extensions import db
from models.data import Data
from schemas.data import DataSchema

data_bp = Blueprint("datas", __name__, url_prefix="/datas")


@data_bp.route('/<int:data_id>', methods=['GET'])
@doc(tags=['data'], description='Get a data')
@use_kwargs({'data_id': fields.Int()}, location='view_args')
@marshal_with(DataSchema)
def get_data(data_id):
    data = Data.query.filter_by(id=data_id).first()
    if not data:
        abort(404, description=f"data.py {data_id} not found")
    return data


@data_bp.route('/', methods=['GET'])
@doc(tags=['data'], description='Get all data')
@marshal_with(DataSchema(many=True))
def get_data_list():
    return Data.query.all()


@data_bp.route('/', methods=['POST'])
@doc(tags=['data'], description='Create a new data.py')
@use_kwargs(DataSchema(exclude=['id']))
@marshal_with(DataSchema)
def post_data(**kwargs):
    data = Data()
    data.sensor_data = kwargs["sensor_data"]
    data.latitude = kwargs["latitude"]
    data.longitude = kwargs["longitude"]
    data.vehicle_id = kwargs["vehicle_id"]
    data.date = kwargs["date"]

    db.session.add(data)
    db.session.commit()

    return data


def register_routes(api):
    api.register_blueprint(data_bp)
