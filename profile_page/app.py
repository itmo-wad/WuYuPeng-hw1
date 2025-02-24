from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Basic route serving static HTML
@app.route('/')
def home():
    # Redirect to profile page
    return redirect(url_for('profile'))

# Advanced route using template rendering
@app.route('/profile')
def profile():
    # Profile data to pass to template
    profile_data = {
        'name': 'Wu Yupeng',
        'title': 'AI Security Software Engineer',
        'bio': 'I am a student, a passionate AI software engineer with a strong background in programming languages, frameworks, design patterns, and best practices.',
        'skills': ['Python', 'Golang', 'LLM', 'Security', 'Kubernetes'],
        'profile_image': url_for('static', filename='images/profile.jpg')
    }
    return render_template('profile.html', profile = profile_data)

if __name__ == '__main__':
    app.run(debug=True)
