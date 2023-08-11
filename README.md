# Real-Time Network traffic visualization Web App with Python FastAPI

Network traffic visualization web app that offers real-time analysis and visualization of network data. Built with Python
![Screenshot of network traffic insight page](https://github.com/creativebash/packet-pulse-insights/blob/main/Screenshot.png)
## Requirements

- Python (>=3.7)
- FastAPI
- Uvicorn

## Getting Started

1. Install the required packages using the following command:

    ```bash
    pip install fastapi uvicorn
    ```

2. Clone this repository and navigate to the project directory:

    ```bash
    git clone https://github.com/creativebash/packet-pulse-insights.git
    cd packet-pulse-insights
    ```

3. Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

4. Open your web browser and visit `http://127.0.0.1:8000/` to access the SIEM tool.

## Features

- The SIEM tool displays security events fetched from the backend API.
- For simplicity, sample security events are used as mock data.

## Notes

- This is a basic proof-of-concept. For a real-world SIEM tool, data collection, correlation, and alerting mechanisms should be more comprehensive.
