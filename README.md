# Sophy

A simple Slack notification utility.

## Installation

```bash
pip install -e .
```

## Usage

```python
from sophy import Sophy

# Set SLACK_TOKEN environment variable first
slack_notifier = Sophy('user@example.com')
slack_notifier.notify('Hello from Sophy!')
```
