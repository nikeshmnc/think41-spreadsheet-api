from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/spreadsheets/<int:spreadsheet_id>/cells/<string:cell_id>/dependents', methods=['GET'])
def get_dependents(spreadsheet_id, cell_id):
    # Placeholder response
    return jsonify({"dependents": ["B2", "C3"]})

@app.route('/spreadsheets/<int:spreadsheet_id>/cells/<string:cell_id>/precedents', methods=['GET'])
def get_precedents(spreadsheet_id, cell_id):
    # Placeholder response
    return jsonify({"precedents": ["A1", "B1"]})

@app.route('/spreadsheets/<int:spreadsheet_id>/recalculation-order', methods=['GET'])
def get_recalculation_order(spreadsheet_id):
    # Placeholder response
    return jsonify({"recalculation_order": ["A1", "B2", "C3"]})

if __name__ == '__main__':
    app.run(debug=True)
