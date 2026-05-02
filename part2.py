# CSC500 Module 3 Critical Thinking Assignment - Part 2
# Author: Andrew Friedrich
# Description: Given the current time on a 24-hour clock and a number of hours
#              to wait, calculate the time the alarm will go off.

def main():
    # Prompt the user for current time and wait duration
    current_time = int(input("Enter the current time in hours (0-23): "))
    wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

    # Use modulo 24 to wrap the result back into the 0-23 range
    alarm_time = (current_time + wait_hours) % 24

    # Display the alarm time
    print(f"\nThe alarm will go off at {alarm_time} on a 24-hour clock.")


if __name__ == "__main__":
    main()
