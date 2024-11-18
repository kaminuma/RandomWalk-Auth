import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# データベース初期化関数
def init_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    # ユーザーテーブルの作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            steps TEXT
        );
    ''')

    conn.commit()
    conn.close()

# 初期化呼び出し
init_db()

# トップページのルート
@app.route('/')
def index():
    return render_template('index.html')

# ユーザー登録エンドポイント
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_id = data.get('user_id')
    steps = data.get('steps')

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (user_id, steps) VALUES (?, ?)
    ''', (user_id, steps))

    conn.commit()
    conn.close()

    return jsonify({"message": "Registration successful!"})

# ユーザー認証エンドポイント
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    user_id = data.get('user_id')
    steps = data.get('steps')

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()

    print(f"Received user_id: {user_id}, steps: {steps}")  # ログ出力

    if user and user[1] == steps:  # steps are matched
        return jsonify({"result": "success"})
    else:
        return jsonify({"result": "fail"})

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
