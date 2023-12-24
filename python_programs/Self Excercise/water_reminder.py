# Water drink reminder
# from win10toast import ToastNotifier

# class Water():
#     def __init__(self):
#         self.drink_time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
#         self.toaster = ToastNotifier()
#     def drink_notification(self, message):
#         self.message = message
#         for time in self.drink_time:
#             self.toaster.show_toast(self.message, duration=10)

# object = Water()
# object.drink_notification(f"REMINDER: It's to have water!!")

import time
from win10toast import ToastNotifier

class WaterReminder:
    def __init__(self):
        self.toaster = ToastNotifier()

    def display_notification(self, message):
        self.message = message
        self.toaster.show_toast("Water Reminder", message, duration=10)

    def run_reminder(self):
        try:
            while True:
                current_time = time.strftime("%H:%M")
                self.display_notification(f"Drink water! Current time: {current_time}")
                time.sleep(3600)  # Sleep for 1 hour
        except KeyboardInterrupt:
            print("Reminder stopped.")

if __name__ == "__main__":
    reminder = WaterReminder()
    print("Water reminder started. Press 'Ctrl+C' to quit.")
    reminder.run_reminder()

# from win10toast import ToastNotifier
# import time
# import datetime

# class WaterReminder:
#     def __init__(self):
#         self.toaster = ToastNotifier()
#         self.quit = False

#     def drink_notification(self):
#         while not self.quit:
#             current_time = datetime.datetime.now().strftime("%H:%M")
#             message = f"REMINDER: It's {current_time}. Time to have water!"
#             self.toaster.show_toast("Water Reminder", message, duration=10)

#             # Wait for an hour
#             time.sleep(30)

#     def start_reminder(self):
#         print("Water reminder started. Press 'q' to quit.")
#         self.drink_notification()

#     def stop_reminder(self):
#         self.quit = True
#         print("Water reminder stopped.")

# if __name__ == "__main__":
#     reminder = WaterReminder()
#     reminder.start_reminder()

#     while True:
#         user_input = input()
#         if user_input.lower() == 'q':
#             reminder.stop_reminder()
#             break
        


