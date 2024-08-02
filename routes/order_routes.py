from flask import Blueprint, request, jsonify
from models.order import create_order, get_order, update_order_status, delete_order

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/order', methods=['POST'])
def create_order_route():
    """API route to create a new order"""
    data = request.get_json()
    order_id = create_order(data['user_id'], data['products'], data['total_price'])
    return jsonify({"id": str(order_id)}), 201

@order_bp.route('/order/<order_id>', methods=['GET'])
def get_order_route(order_id):
    """API route to retrieve order information"""
    order = get_order(order_id)
    if order:
        return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404

@order_bp.route('/order/<order_id>', methods=['PUT'])
def update_order_route(order_id):
    """API route to update order status"""
    data = request.get_json()
    result = update_order_status(order_id, data['status'])
    if result.modified_count > 0:
        return jsonify({"message": "Order status updated"}), 200
    return jsonify({"error": "Order not found"}), 404

@order_bp.route('/order/<order_id>', methods=['DELETE'])
def delete_order_route(order_id):
    """API route to delete an order"""
    result = delete_order(order_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Order deleted"}), 200
    return jsonify({"error": "Order not found"}), 404
