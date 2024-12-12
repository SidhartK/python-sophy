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
sophy = Sophy('user@example.com')
sophy.notify('Hello from Sophy!')
```
