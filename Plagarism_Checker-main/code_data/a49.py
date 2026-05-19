import time
import threading

def set_reminder(reminder, delay):
    time.sleep(delay)
    print(f"Reminder: {reminder}")

def main():
    print("Welcome to the Reminder Application!")
    
    while True:
        reminder = input("Enter a reminder (or type 'exit' to quit): ")
        if reminder.lower() == 'exit':
            print("Exiting the reminder application.")
            break
        
        delay = int(input("Enter delay in seconds: "))
        reminder_thread = threading.Thread(target=set_reminder, args=(reminder, delay))
        reminder_thread.start()
        print(f"Reminder set for {delay} seconds.")

if __name__ == "__main__":
    main()
