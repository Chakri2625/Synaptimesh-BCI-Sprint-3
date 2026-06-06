# BCI Command Dispatcher System

## Sprint 3 – Day 4
### Logging, Error Handling & System Validation

---

## Project Description

The BCI Command Dispatcher System simulates a Brain-Computer Interface (BCI) backend capable of receiving classified commands and executing automation actions on a computer.

The system includes:

- Command Dispatching
- Confidence Validation
- Structured Logging
- Error Handling
- MQTT Messaging
- Automation Execution
- Unit Testing
- Full System Integration Testing

---

## Features

### Structured Logging

All command activity is recorded in:

logs/command_log.txt

Logged events include:

- Command received
- Command executed
- MQTT connection events
- MQTT published messages
- MQTT received messages
- Errors and exceptions

Example:

```text
2025-06-06 14:38:02 - INFO - Received command: OPEN_BROWSER
2025-06-06 14:38:02 - INFO - Successfully executed: OPEN_BROWSER
```

---

## Error Handling

### Backend Layer

Implemented in:

```text
app/dispatcher.py
app/exceptions.py
```

Custom Exceptions:

```python
InvalidCommandError
AutomationExecutionError
```

Capabilities:

- Detect invalid commands
- Catch automation failures
- Prevent system crashes
- Return structured error responses
- Log all errors

---

### Automation Layer

Implemented in:

```text
app/automations/
```

Modules:

- browser.py
- media.py
- mouse.py
- applications.py

Capabilities:

- Execute desktop automation
- Handle execution failures
- Report errors to dispatcher

---

### MQTT Layer

Implemented in:

```text
app/mqtt/
```

Files:

```text
publisher.py
subscriber.py
```

Capabilities:

- Publish commands
- Subscribe to commands
- Dispatch commands automatically
- Log MQTT activity
- Handle connection interruptions

---

## Supported Commands

### Browser Commands

```text
OPEN_BROWSER
CLOSE_BROWSER
OPEN_YOUTUBE
```

### Media Commands

```text
PLAY_PAUSE
VOLUME_UP
VOLUME_DOWN
MUTE
```

### Mouse Commands

```text
SCROLL_UP
SCROLL_DOWN
MOUSE_LEFT
MOUSE_RIGHT
MOUSE_UP
MOUSE_DOWN
```

### Application Commands

```text
OPEN_NOTEPAD
CLOSE_NOTEPAD

OPEN_CALCULATOR
CLOSE_CALCULATOR
```

---

## Project Structure

```text
backend/
│
├── app/
│   │
│   ├── automations/
│   │   ├── browser.py
│   │   ├── media.py
│   │   ├── mouse.py
│   │   └── applications.py
│   │
│   ├── mqtt/
│   │   ├── publisher.py
│   │   └── subscriber.py
│   │
│   ├── command_registry.py
│   ├── dispatcher.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── reference_signal.py
│   ├── signal_runner.py
│   └── validator.py
│
├── logs/
│   └── command_log.txt
│
├── tests/
│   ├── test_dispatcher.py
│   ├── test_validator.py
│   └── test_logger.py
│
├── demo_runner.py
├── demo.py
├── requirements.txt
└── README.md
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Demo

### Run Reference Signal Demo

```bash
python demo_runner.py
```

This will:

- Validate confidence scores
- Dispatch commands
- Execute automation
- Generate logs

---

## MQTT Testing

### Start Subscriber

Open Terminal 1:

```bash
python -m app.mqtt.subscriber
```

---

### Start Publisher

Open Terminal 2:

```bash
python -m app.mqtt.publisher
```

---

Expected Flow:

```text
Publisher
    ↓
MQTT Broker
    ↓
Subscriber
    ↓
Dispatcher
    ↓
Automation Layer
    ↓
Logger
```

---

## Unit Testing

Run all tests:

```bash
python -m pytest tests -v
```

Example:

```text
3 passed
0 failed
```

---

## Full System Integration Test

Validated Components:

- Logger
- Validator
- Dispatcher
- Command Registry
- Automation Layer
- MQTT Publisher
- MQTT Subscriber
- Demo Runner

Results:

```text
10/10 Commands Processed Successfully
```

---

## Validation Checklist

Completed:

- Structured Logging Module
- Error Handling – Backend Server Layer
- Error Handling – Automation Layer
- Error Handling – MQTT Layer
- Unit Testing with pytest
- Full System Integration Test
- Sprint Demo Script
- Code Review
- Documentation

---

## Code Review Summary

### Logger Module

Verified:

- Logs created successfully
- Commands recorded correctly
- MQTT events recorded correctly

Status:

PASS

---

### Dispatcher Module

Verified:

- Invalid commands handled
- Exceptions caught properly
- Structured responses returned

Status:

PASS

---

### Automation Modules

Verified:

- Browser automation
- Media controls
- Mouse controls
- Application controls

Status:

PASS

---

### MQTT Modules

Verified:

- Publisher sends messages
- Subscriber receives messages
- Commands dispatched automatically
- Events logged

Status:

PASS

---

### Unit Tests

Verified:

- Dispatcher tests
- Validator tests
- Logger tests

Status:

PASS

---

## Sprint Status

Sprint 3 – Day 4

Status:

COMPLETED

All logging, error handling, MQTT integration, unit testing, and full system validation requirements have been successfully implemented and verified.