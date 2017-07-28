from elasticsearch import Elasticsearch

from app.preprocessing.preprocessing import Preprocessing


class DataIndexing:

    def __init__(self):
        self.es = Elasticsearch('http://localhost:9200', verify_certs=True, timeout=2, port=443, use_ssl=False)
        self.preprocess = Preprocessing()

    def populate(self,data):

        type_ = data['type']

        db_data = data["entries"]

        for data_ in db_data:

            pos_noun_tags, pos_adj_tags, pos_verb_tags = self.preprocess.get_pos_tags(data_['text'])
            pos = {"text_pos":{"noun":pos_noun_tags,"verb":pos_verb_tags,"adjective":pos_adj_tags}}
            data_.update(pos)

            self.es.index(index='kb',doc_type=type_,body=data_)



