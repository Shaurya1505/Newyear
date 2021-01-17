from win10toast import ToastNotifier
notification = ToastNotifier()

jobs = [
    ["Sleep early"],
    ["Wake up early"],
    ["brush daily"],
    ["study"],
    ["go for a run"],
    ["clean your room"]
]

for job in jobs:
    notification.show_toast(job[0], job[1], duration = 10)