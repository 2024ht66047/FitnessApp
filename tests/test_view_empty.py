from unittest.mock import patch

def test_view_with_no_entries(tracker_app):
    """
    Should show a message if no workouts are present.
    """
    with patch("tkinter.messagebox.showinfo") as mock_info:
        tracker_app.view_workouts()

    mock_info.assert_called_once_with("Workouts", "No workouts logged yet.")

