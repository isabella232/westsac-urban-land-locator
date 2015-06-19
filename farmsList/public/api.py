import jsonpickle

from flask import Blueprint
from farmsList.public.models import Parcel

blueprint = Blueprint('api', __name__, url_prefix='/api',
						static_folder="../static")

@blueprint.route("/parcel/", methods=["GET", "POST"])
def api_parcel():
	print "HELLO"
	parcelData = Parcel.query.filter(Parcel.listedToPublic == True).all()
	print "HELLO 2"
	return jsonpickle.encode(parcelData, unpicklable=False, make_refs=False)