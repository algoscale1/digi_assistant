from flask import request
from . import routes
from .exceptions import InvalidUsage, DataNotFound, ElasticsearchTimeout
import json
import logging
from app.es_interface.mural_indexing import DataIndexing


logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger('digi_assistant')


indexing = DataIndexing()


@routes.route('/ingest', methods=['POST'])
def index_data():

    data = request.get_json(force=True)

    indexing.populate(data)

    response = {"status": "success", "status_code": 200}

    return json.dumps(response)
