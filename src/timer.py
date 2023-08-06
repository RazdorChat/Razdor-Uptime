from apscheduler.schedulers.background import BlockingScheduler
def print_t():
  print("hello")
  print("bye")

sched = BlockingScheduler()
sched.add_job(print_t, 'interval', seconds = 60) #will do the print_t work for every 60 seconds

sched.start()