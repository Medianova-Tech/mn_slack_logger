
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
  pip install git+https://github.com/Medianova-Tech/mn_slack_logger.git
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

You can use the slack_log method of MN Slack Logger to send error messages to your Slack channel. Here's a simple example:

```sh
from mn_slack_logger import slack_log

params = {"param1": "value1", "param2": "value2"}
headers = {"header1": "value1", "header2": "value2"}
error_info = "Example error info"

# Sending log to Slack
slack_log(message="your error message", slack_url="Your slack hook", username="Your user name", level="error",
          url="https://github.com/yourusername/mn-slack-logger", params=params,
          headers=headers, error=error_info)

  ```
<p align="right">(<a href="#top">back to top</a>)</p>


