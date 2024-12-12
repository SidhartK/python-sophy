# Sophy

A simple Slack notification utility.

## Installation

```bash
pip install sophy-python
```

## Usage

```python
from sophy import Sophy

# Set SLACK_TOKEN environment variable first
slackbot = Sophy('user@example.com')
slackbot.notify('Hello World!')
```
