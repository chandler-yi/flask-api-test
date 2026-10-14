from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟一个“数据库”
items = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "FastAPI"},
]

# GET：获取所有数据
@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify({"items": items})

# GET：根据 id 获取单个数据
@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "not found"}), 404

# POST：新增数据
@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400

    new_item = {
        "id": len(items) + 1,
        "name": data["name"],
    }
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)