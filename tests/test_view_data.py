from unittest.mock import patch

def test_view_with_existing_entries(tracker_app):
    """
    Should display the logged workouts in formatted form.
    """
    tracker_app.workouts = [
        {"workout": "Cycling", "duration": 60},
        {"workout": "Pilates", "duration": 35},
    ]

    with patch("tkinter.messagebox.showinfo") as mock_info:
        tracker_app.view_workouts()

    formatted = (
        "Logged Workouts:\n"
        "1. Cycling - 60 minutes\n"
        "2. Pilates - 35 minutes\n"
    )
    mock_info.assert_called_once_with("Workouts", formatted)

