
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Medianova-Tech/mn_slack_logger" id="top">
    <img src="http://medianova-logo.mncdn.com/logo-m.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Medianova Slack Logger</h3>

  <p align="center">
    MN Slack Logger is a Python package for logging error messages to a Slack channel.
  </p>
</div>


<!-- GETTING STARTED -->
## Getting Started

To use MN Slack Logger, follow these steps:

### Prerequisites

First, add MN Slack Logger to your project
  ```sh
  pip install mn-slack-logger
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

MN Slack Logger can be used to send messages of various levels (info, warning, error) to your Slack channel. Here's how you can use it:

```python
from mn_slack_logger import SlackLogger

logger = SlackLogger(slack_url="https://slack-webhook-url", slack_user="Logger")
logger.log("An example message", level="info")
logger.log("An example warning", level="warning")
logger.log("An example error", level="error", error="traceback text...")
  ```

For handling long traceback messages, MN Slack Logger shortens them automatically to fit Slack's message length limits.
<p align="right">(<a href="#top">back to top</a>)</p>

## Usage with FastAPI

MN Slack Logger can be integrated into a FastAPI application to log messages to Slack. Here's an example of how you can use it in your FastAPI application:

```python
from fastapi import FastAPI, HTTPException
from mn_slack_logger import SlackLogger

app = FastAPI()
logger = SlackLogger(slack_url="https://slack-webhook-url", slack_user="FastAPI Logger")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.log(f"HTTP Exception: {exc.detail}", level="error", error=str(exc))
    return {"detail": exc.detail}

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/error")
async def cause_error():
    raise HTTPException(status_code=400, detail="This is a test error")
  ```

This example sets up a basic FastAPI application with an exception handler that logs HTTP exceptions to Slack using MN Slack Logger.
<p align="right">(<a href="#top">back to top</a>)</p>
