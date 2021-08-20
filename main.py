from bson import ObjectId
from faker import Faker
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import *
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/testbase'}
db = MongoEngine(app)
api = Api(app)
fake = Faker()


class Product(db.Document):
    title = StringField(required=True, max_length=30)
    description = StringField(required=True, max_length=150)


class ProductsList(Resource):
    def get(self, slug=None):
        # TODO эту часть включить при первом гет запросе чтоб заполнить базу. потом убрать или так же закоментировать
        # if len(Product.objects.all()) < 1 :
        #     for _ in range(21):
        #         obj = Product(title=fake.text(max_nb_chars=20), description=fake.text(max_nb_chars=50))
        #         obj.save()
        if request.args:
            objects_products = Product.objects.all()
            for filter_key, filter_value in dict(request.args).items():
                if filter_key in Product()._data.keys():
                    objects_products = objects_products.filter(**{filter_key: filter_value})
                elif filter_key in ('order',):
                    return jsonify(Product.objects.order_by('-title').all())
                else:
                    return jsonify('Некорректный фильтр')
            return jsonify(objects_products)
        if slug is None:
            if Product.objects.all():
                return jsonify(Product.objects.all())
            return 'No data'
        else:
            return jsonify(Product.objects(_id=ObjectId(slug)))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('description')
        param = parser.parse_args()
        if all(param.values()):
            obj = Product(title=param['title'], description=param['description'])
            obj.save()
            return jsonify(obj)
        else:
            return 'missing title or description'


api.add_resource(ProductsList, "/", "/", "/<string:slug>")
app.run()
