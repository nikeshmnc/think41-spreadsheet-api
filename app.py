from flask import Flask, jsonify

app = Flask(__name__)

# ✅ Home route to confirm server is running
@app.route('/')
def home():
    return "Think41 Spreadsheet API is running."

# Get Dependents Endpoint
@app.route('/spreadsheets/<int:spreadsheet_id>/cells/<string:cell_id>/dependents', methods=['GET'])
def get_dependents(spreadsheet_id, cell_id):
    dependents = ["B2", "C3", "D4"]
    return jsonify({"dependents": dependents}), 200

# Get Precedents Endpoint
@app.route('/spreadsheets/<int:spreadsheet_id>/cells/<string:cell_id>/precedents', methods=['GET'])
def get_precedents(spreadsheet_id, cell_id):
    precedents = ["A1", "A2"]
    return jsonify({"precedents": precedents}), 200

# Get Recalculation Order Endpoint
@app.route('/spreadsheets/<int:spreadsheet_id>/recalculation-order', methods=['GET'])
def get_recalculation_order(spreadsheet_id):
    recalculation_order = ["A1", "B2", "C3"]
    return jsonify({"recalculation_order": recalculation_order}), 200

if __name__ == '__main__':
    app.run(debug=True)
