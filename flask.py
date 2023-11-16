from flask import Flask, render_template, request

app = Flask(__name__)

# Example club data
clubs = [
    {"name": "Commit the Change", "major": "Computer Science", "description": "A club for CS majors."},
    # ... (more clubs)
]

@app.route('/', methods=['GET'])
def index():
    selected_major = request.args.get('major', 'all')
    sorted_order = request.args.get('sort', 'asc')

    # Filter clubs based on major
    filtered_clubs = [club for club in clubs if club['major'] == selected_major or selected_major == 'all']

    # Sort clubs by name
    filtered_clubs.sort(key=lambda x: x['name'], reverse=(sorted_order == 'desc'))

    return render_template('destination.html', clubs=filtered_clubs)

if __name__ == '__main__':
    app.run(debug=True)
