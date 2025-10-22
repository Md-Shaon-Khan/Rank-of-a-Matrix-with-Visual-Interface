from flask import Flask, render_template, request, jsonify
import numpy as np
import io
import csv

app = Flask(__name__)

def parse_matrix_from_text(text):
    """
    Parse CSV-like text into a 2D float numpy array.
    Accepts rows separated by newline and columns by comma or spaces.
    """
    rows = []
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        # try comma first, else split by whitespace
        if ',' in line:
            parts = [p.strip() for p in line.split(',')]
        else:
            parts = line.split()
        row = [float(p) for p in parts if p != '']
        rows.append(row)
    if not rows:
        raise ValueError("No data")
    # ensure consistent column counts
    cols = len(rows[0])
    for r in rows:
        if len(r) != cols:
            raise ValueError("Inconsistent number of columns in rows.")
    return np.array(rows, dtype=float)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/rank', methods=['POST'])
def compute_rank():
    """
    Accepts form-data fields:
      - matrix_text : raw text matrix (optional)
      - csv_file : uploaded CSV file (optional)
    Returns JSON: {"rank": n}
    """
    try:
        if 'csv_file' in request.files and request.files['csv_file'].filename:
            f = request.files['csv_file']
            stream = io.StringIO(f.stream.read().decode('utf-8'))
            reader = csv.reader(stream)
            rows = []
            for row in reader:
                if not row:
                    continue
                rows.append([float(x) for x in row if x != ''])
            mat = np.array(rows, dtype=float)
        else:
            text = request.form.get('matrix_text', '')
            mat = parse_matrix_from_text(text)

        rank = int(np.linalg.matrix_rank(mat))
        return jsonify({"rank": rank})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
