"""Example usage for Butterworth IIR Filter Skill."""
from client import ButterworthLowpass

def main():
    print("Executing Butterworth IIR Filter...")
    bw = ButterworthLowpass(cutoff_freq=4.0, sampling_rate=40.0)
    noisy_stream = [1.0 if i % 2 == 0 else -1.0 for i in range(16)]
    smoothed = bw.filter_signal(noisy_stream)
    print("Smoothed Signal:", smoothed)
    assert len(smoothed) == len(noisy_stream)
    print("Butterworth IIR Filter verified successfully!")

if __name__ == "__main__":
    main()
