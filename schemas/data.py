from marshmallow import fields, Schema


class DataSchema(Schema):
    id = fields.Int()
    vehicle_id = fields.Str()
    latitude = fields.Str()
    longitude = fields.Str()
    sensor_data = fields.Str()
    date = fields.Str()
