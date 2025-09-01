from unittest.mock import patch

def test_add_fails_with_empty_fields(tracker_app):
    """
    Adding without workout/duration should fail and not update list.
    """
    tracker_app.workout_entry.insert(0, "")
    tracker_app.duration_entry.insert(0, "")

    with patch("tkinter.messagebox.showerror") as mock_error:
        tracker_app.add_workout()

    assert tracker_app.workouts == []
    mock_error.assert_called_once_with("Error", "Please enter both workout and duration.")

