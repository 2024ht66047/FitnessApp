from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

# In a real application, this would be a database
workouts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        workout = request.form.get('workout')
        duration_str = request.form.get('duration')

        if not workout or not duration_str:
            flash('Please enter both workout and duration.', 'error')
        else:
            try:
                duration = int(duration_str)
                workouts.append({'workout': workout, 'duration': duration})
                flash(f"'{workout}' added successfully!", 'success')
            except ValueError:
                flash('Duration must be a number.', 'error')

        # Redirect to the same page to prevent form resubmission
        return redirect(url_for('index'))

    return render_template('index.html', workouts=workouts)

if __name__ == '__main__':
    app.run(debug=True)