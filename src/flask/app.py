from flask import Flask, render_template, request, redirect, url_for
from pypg import helper
import json


app = Flask(__name__)

@app.route('/')
def index():
  tables = helper.read_tables()
  return render_template("index.html", table=[0][0])


@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    phone = request.form.get("phone")

    print(f"{name}이 {phone}로 가입")
    print(helper.insert("student", name, phone))

    return render_template("index.html")


@app.route('/select', methods=["POST"])
def select():
  name = request.form["name_to_search"]
  result = helper.select("student", name)
  
  print(f"{name} 검색결과 : {result}")

  result = json.dumps(result, ensure_ascii=False)
 
  return result


@app.route('/count', methods=["POST"])
def count():
  name = request.form["name_to_count"]
  result = helper.count("student", name)
  result=json.dumps(result)

  print(f"{name}과 검색결과가 유사한 총 개수: {result}")
  
  return result


@app.route('/delete', methods=["POST"])
def delete():
    name = request.form["name_to_delete"]

    print(f"{name} 삭제")
    print(helper.delete("student",name))

    return render_template("index.html")


@app.route('/update', methods=["POST"])
def update():
  name = request.form["name_to_update"]
  phone = request.form["phone_to_update"]

  print(f"{name}, {phone} 수정")
  print(helper.update("student", name, phone))

  return render_template("index.html")


@app.route("/list-rest")
def students_list_rest():
  result = helper.students_list() #list type -> column 으로 접근
  result = json.dumps(result)
  print(f"{result}")
  return result


if __name__ == ("__main__"):
  # docker
  app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  #app.run(debug=True)



