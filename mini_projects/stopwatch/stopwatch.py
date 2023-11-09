import tkinter as Tkinter
import time


class StopWatch:
    def __init__(self):
        self._state = "clear"
        self._start_time = 0
        self._elapsed_time = 0

    ''' Getters and Setters '''
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def elapsed_time(self):
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, value):
        self._elapsed_time = value

    ''' Class methods '''
    def start(self):
        if self.state != "running":
            self.state = "running"
            self.start_time = time.time() - self.elapsed_time
            print("Stopwatch started.")

    def pause(self):
        if self.state == "running":
            self.state = "paused"
            self.elapsed_time = time.time() - self.start_time
            print("Stopwatch paused.")

    def reset(self, curr_label):
        if self.state == "paused":
            self.state = "clear"
            self.elapsed_time = 0
            self.start_time = 0
            curr_label['text'] = self.format_time(0)
        else:
            self.elapsed_time = 0
            self.start_time = time.time()
            curr_label['text'] = self.format_time(0)
        print("Stopwatch reset.")

    def get_elapsed_time(self):
        if self.state == "running":
            return time.time() - self.start_time
        else:
            return self.elapsed_time

    def timer(self, curr_label):
        def count():
            if self.state == "running":
                curr_time = self.format_time(self.get_elapsed_time())
                curr_label['text'] = curr_time
                curr_label.after(50, count)
        count()

    @staticmethod
    def format_time(elap):
        hours = int(elap / 3600)
        minutes = int(elap / 60 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes * 60.0)
        hseconds = int((elap - hours * 3600.0 - minutes * 60.0 - seconds) * 10)
        return '%02d:%02d:%02d:%1d' % (hours, minutes, seconds, hseconds)


# define root window and set fixed min size and title
root = Tkinter.Tk()
root.title("Best Stopwatch Worldwide")
root.minsize(width=500, height=500)

# define ready label
label = Tkinter.Label(root, text='Ready!', fg='white', font='Verdana 40 bold')
label.pack(pady=150)

# create stop watch instance
stop_watch = StopWatch()

# define a frame and buttons
buttonFrame = Tkinter.Frame(root)
Tkinter.Button(buttonFrame, text='Start', width=6, command=lambda: (stop_watch.start(), stop_watch.timer(label))).pack(side='left')
Tkinter.Button(buttonFrame, text='Pause', width=6, command=stop_watch.pause).pack(side='left')
Tkinter.Button(buttonFrame, text='Reset', width=6, command=lambda: stop_watch.reset(label)).pack(side='left')
buttonFrame.pack(anchor='center', pady=5)
root.mainloop()
