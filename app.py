# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:06:53 2024

@author: hh
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process_text():
    text = request.form['text']
    sentences = text.split('.')  # 简单地以句号分割文本来获取句子
    return render_template('process.html', sentences=sentences)

@app.route('/submit', methods=['POST'])
def submit():
    # 这里你可以处理表单提交的数据
    # 例如，保存用户的评价和评论到文件或数据库
    return "评价已保存！"  # 或者重定向到一个新的页面

if __name__ == '__main__':
    app.run(debug=True)
