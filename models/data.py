from extensions import db


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(36), nullable=False)
    latitude = db.Column(db.String(36), nullable=False)
    longitude = db.Column(db.String(36), nullable=False)
    sensor_data = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
