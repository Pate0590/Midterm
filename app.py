from flask import Flask, jsonify, request

from flask import Flask, jsonify, request
Student = {
        '1': {'id': '1','name': 'Ankit', 'grade': 'A'},
        '2': {'id': '1','name': 'Nirmal ', 'grade': 'b'}
}

app = Flask(__name__)

@app.route('/student/<id>')
def student(id):

    student_info = Student.get(id, {})
    print(student_info)
    return jsonify(student_info)

@app.route('/student', methods=['POST'])
def create_student():
    new_student = request.get_json()
    
    
    required_keys = ['id','name', 'grade']
    if all(key in new_student for key in required_keys):
        Student[str(len( Student.keys()) + 1)] = new_student
        print( Student)
        return jsonify({"success":True})
    else:
        return jsonify({"success":False, "msg": "Please pass all the data"})
    
@app.route('/student/<id>', methods=['PUT'])
def update_student(id):
 
    if id in  Student:
        updated_student = request.get_json()

        required_keys = ['id','name', 'grade']
        if all(key in updated_student for key in required_keys):
            Student[id] = updated_student
            print( Student)
            return jsonify({"success": True, "msg": "Student updated successfully"})
        else:
            return jsonify({"success": False, "msg": "Please pass all the required data for update"}), 400
    else:
        return jsonify({"success": False, "msg": "student not found"}), 404
    
@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
    if id in  Student:
       
        del  Student[id]
        return jsonify({"success": True, "msg": "student deleted successfully"})
    else:
        return jsonify({"success": False, "msg": "student not found"}), 404





if __name__ == '__main__':
    app.run('0.0.0.0',port=5001)