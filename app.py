from flask import Flask, jsonify
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/random-bit', methods=['GET'])
def get_random_bit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()

    bit = list(counts.keys())
    return jsonify({'bit': bit})

if __name__ == '__main__':
    app.run()
