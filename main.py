from flask import Flask, render_template, request

app = Flask(__name__)

contact = '''        
<ul class="nav-wrapper">
            <li class="contact">
                <a href="https://t.me/Xbasan">
                    <img class=img-icon src="static/img/tg.svg">
                </a>
            </li>
            <li class="contact">
                <a href="https://github.com/Xbasan">
                    <img class=img-icon src="static/img/git.svg">
                </a>
            </li>
            <li class="contact">
                <a href="mailto:xamzpok@gmail.com">
                    <img class=img-icon src="static/img/gmail.svg">
                </a>
            </li>
        </ul>'''

@app.route('/', methods=['GET'])
def main( ):
    return render_template('index.html', contact=contact)

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html', contact=contact)

if __name__ == '__main__':
    app.run(debug=True,
              host='0.0.0.0') # 6969