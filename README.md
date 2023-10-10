# Event Calendar Python Application

## Overview

This Python application is a simple event/calendar manager designed to help users keep track of events, assignments, and due dates. The application reads event data from a .txt file, processes it, and displays the events on a graphical user interface (GUI) calendar. Users can interact with the calendar to view, add, and delete events.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Read event data from a .txt file in the format "EventID-M-D-YYY-Assignment_Name."
- Display events on a calendar using a graphical user interface.
- View event details for a specific date by selecting the date and clicking the "Display" button.
- Delete events that are no longer needed by selecting the event and clicking the "Delete Event" button.

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/Devamp/event-calendar.git
   ```

2. Navigate to the project directory:

```
    cd event-calendar
```

3. Install required Python libraries:

```
    pip install tkcalendar
```

## Usage

1. Create a .txt file with event data in the following format: "EventID-M-D-YYY-Assignment_Name."

```
    7-1-29-2001-Devam’s_Birthday
```

2. Run application:

```
    python3 app.py
```

When prompted will file input, enter in the sample .txt file created in previous step.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or create a pull request. Your contributions are welcome!

## License

This project is licensed under the MIT License.
