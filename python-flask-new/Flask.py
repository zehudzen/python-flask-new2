# Description: Flask ile basit bir REST API uygulaması  (Python 3.6.5)  
from flask import Flask, jsonify, request

app = Flask(__name__)

# Örnek bir veri kümesi
tasks = [
    {
        'id': 1,
        'title': 'Görev 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Görev 2',
        'done': False
    }
]

# Tüm görevleri getiren endpoint
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Belirli bir görevi getiren endpoint
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Görev bulunamadı'}), 404
    return jsonify({'task': task})

# Yeni bir görev ekleyen endpoint
@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Geçersiz istek'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(new_task)

    return jsonify({'task': new_task}), 201

# Ana uygulamayı çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
