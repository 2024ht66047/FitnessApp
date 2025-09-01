import pytest
import tkinter as tk
from src.ACEest_Fitness import FitnessTrackerApp

@pytest.fixture(scope="function")
def tracker_app():
    """
    Fixture to create and cleanup FitnessTrackerApp instance.
    """
    root = tk.Tk()
    root.withdraw()
    app = FitnessTrackerApp(root)
    yield app
    root.destroy()
