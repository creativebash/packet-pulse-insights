# Real-Time Web-based Network Traffic Visualization and Analysis

Network traffic visualization web app that offers real-time analysis and visualization of network data. Built with Python.
![Screenshot of network traffic insight page](https://github.com/creativebash/packet-pulse-insights/blob/main/Screenshot.png)

## Requirements

- Python (>=3.7)

## Getting Started

1. Clone this repository and navigate to the project directory:

    ```bash
    git clone https://github.com/creativebash/packet-pulse-insights.git
    cd packet-pulse-insights
    ```

2. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

5. Open your web browser and visit `http://127.0.0.1:8000/web/events` to access the SIEM tool.

## Features

- The SIEM tool displays security events fetched from the backend API.
- For simplicity, sample security events are used as mock data.

## Notes

- This is a basic proof-of-concept. For a real-world SIEM tool, data collection, correlation, and alerting mechanisms should be more comprehensive.
