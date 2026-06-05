import time

from app.reference_signal import REFERENCE_SIGNALS
from app.dispatcher import dispatch_command
from app.validator import is_valid_confidence


def run_reference_signals():

    print("\n===== BCI Reference Signal Demo Started =====\n")

    for signal in REFERENCE_SIGNALS:

        signal_id = signal["signal_id"]
        correlation_id = signal["correlation_id"]
        command = signal["command"]
        confidence = signal["confidence"]
        target = signal["target"]

        print(f"\nSignal ID      : {signal_id}")
        print(f"Correlation ID : {correlation_id}")
        print(f"Command        : {command}")
        print(f"Confidence     : {confidence}")
        print(f"Target         : {target}")

        if is_valid_confidence(confidence):

            result = dispatch_command(command)

            print("Result:", result)

        else:

            print(
                f"Rejected: confidence {confidence} below threshold"
            )

        print("-" * 60)

        time.sleep(5)

    print("\n===== Demo Completed =====")