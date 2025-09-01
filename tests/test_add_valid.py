from unittest.mock import patch

def test_workout_added_correctly(tracker_app):
    """
    Ensure adding a valid workout updates the workouts list.
    """
    tracker_app.workout_entry.insert(0, "Swimming")
    tracker_app.duration_entry.insert(0, "40")

    with patch("tkinter.messagebox.showinfo") as mock_success:
        tracker_app.add_workout()

    assert len(tracker_app.workouts) == 1
    assert tracker_app.workouts[0] == {"workout": "Swimming", "duration": 40}
    mock_success.assert_called_once_with("Success", "'Swimming' added successfully!")

