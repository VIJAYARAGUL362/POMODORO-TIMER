# Pomodoro Timer - Tkinter Application

This Python application implements a simple Pomodoro Timer using the Tkinter library for the graphical user interface. It helps users manage their time by alternating between focused work intervals and short/long breaks.

**This project was created as part of the learning process from Dr. Angela Yu's "100 Days of Code in Python" course.**

## Features

* **Customizable Timer:** Sets work intervals (default: 25 minutes), short break intervals (default: 5 minutes), and a long break interval (default: 20 minutes).
* **Visual Countdown:** Displays a clear countdown timer in minutes and seconds.
* **Work/Break Indication:** Clearly labels the current session as either "TIMER" (work) or "BREAK".
* **Progress Tracking:** Shows checkmarks to indicate the completion of work sessions.
* **Start and Reset Buttons:** Allows users to start and reset the timer as needed.
* **Graphical User Interface:** Built with Tkinter for a simple and intuitive desktop experience.

## How to Use

1.  **Prerequisites:**
    * Python 3 must be installed on your system.
    * Tkinter is usually included with standard Python installations.
    * Ensure the `tomato.png` image file is in the same directory as the Python script. You can find this image in many online resources or replace it with your own.

2.  **Running the Application:**
    * Save the Python code you provided as a `.py` file (e.g., `pomodoro_timer.py`).
    * Place the `tomato.png` image file in the same directory as the Python script.
    * Open your terminal or command prompt.
    * Navigate to the directory where you saved the files using the `cd` command.
    * Run the script using the Python interpreter:
        ```bash
        python pomodoro_timer.py
        ```
    * The Pomodoro Timer window will appear.
    * Click the "Start" button to begin the timer. It will cycle through work and break periods.
    * Click the "Reset" button to stop the timer and reset it to the initial state.

## Code Structure

* **`CONSTANTS`:** Defines various parameters for the timer, such as colors, font, and durations of work and break intervals.
* **`resetting_button()`:** Function called when the "Reset" button is pressed, resetting the timer.
* **`timer_mechanism()`:** Function that controls the sequence of work and break periods based on the number of repetitions.
* **`counting_number(count)`:** Function responsible for the countdown mechanism, updating the timer display on the GUI.
    * **UI Setup:** The main part of the script that uses Tkinter to create the application window, labels, buttons, and canvas for the tomato image and timer display.

## Customization

You can customize the timer by modifying the constants defined at the beginning of the script:

* `WORK_MIN`: Duration of work intervals in minutes (default: 25).
* `SHORT_BREAK_MIN`: Duration of short breaks in minutes (default: 5).
* `LONG_BREAK_MIN`: Duration of the long break in minutes (default: 20).
* You can also change the colors, font, and other UI elements within the Tkinter setup section.

## License

This project was created as part of the learning process from Dr. Angela Yu's "100 Days of Code in Python" course. As such, it is intended for educational and personal use.

If you are considering using this code for commercial purposes or redistribution, please be mindful of the original source and consider the appropriate open-source license. Some common open-source licenses include the MIT License, Apache License 2.0, and GNU GPLv3. You can learn more about these licenses at [https://choosealicense.com/](https://choosealicense.com/).

**Attribution:**

While not a formal license requirement for personal projects based on tutorials, it's good practice to acknowledge the source of your learning. You might consider adding a line in your `README.md` or comments in your code mentioning Dr. Angela Yu's course.

---

**To use this `README.md` file:**

1.  Save the text above as a file named `README.md` in the same directory as your Python script (`pomodoro_timer.py`) and the `tomato.png` image.
2.  When you upload your code to GitHub, this file will be automatically displayed on the repository's main page, providing information about your project.
