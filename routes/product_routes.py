from flask import Blueprint, request, jsonify
from models.product import add_product, get_product, update_product, delete_product

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/product', methods=['POST'])
def create_product():
    """API route to create a new product"""
    data = request.get_json()
    product_id = add_product(data['name'], data['description'], data['price'], data['category_id'])
    return jsonify({"id": str(product_id)}), 201

@product_bp.route('/product/<product_id>', methods=['GET'])
def get_product_route(product_id):
    """API route to retrieve product information"""
    product = get_product(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@product_bp.route('/product/<product_id>', methods=['PUT'])
def update_product_route(product_id):
    """API route to update product information"""
    data = request.get_json()
    result = update_product(product_id, data)
    if result.modified_count > 0:
        return jsonify({"message": "Product updated"}), 200
    return jsonify({"error": "Product not found"}), 404

@product_bp.route('/product/<product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    """API route to delete a product"""
    result = delete_product(product_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Product deleted"}), 200
    return jsonify({"error": "Product not found"}), 404
