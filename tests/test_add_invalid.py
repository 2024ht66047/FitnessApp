from unittest.mock import patch

def test_add_fails_with_non_numeric_duration(tracker_app):
    """
    Duration must be numeric; otherwise show error.
    """
    tracker_app.workout_entry.insert(0, "Jogging")
    tracker_app.duration_entry.insert(0, "NaN")

    with patch("tkinter.messagebox.showerror") as mock_error:
        tracker_app.add_workout()

    assert tracker_app.workouts == []
    mock_error.assert_called_once_with("Error", "Duration must be a number.")

