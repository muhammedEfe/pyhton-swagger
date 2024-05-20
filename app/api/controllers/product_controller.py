from flask_restx import Resource, Namespace

ns = Namespace('products', description='Product operations')

@ns.route('/productGet')
class ProductGet(Resource):
    def get(self):
        return {"message": "Product Get completed"}

@ns.route('/productSet')
class ProductSet(Resource):
    def post(self):
        return {"message": "Product Set completed"}

    def get(self):
        return {"message": "Product Get completed"}
@ns.route('/productDelete')
class ProductDelete(Resource):
    def delete(self):
        return {"message": "Product Set completed"}

@ns.route('/productFilter/<id>')
class ProductFilter(Resource):
    def get(self, id):
        return {"message": "Product Set completed "+ id}

