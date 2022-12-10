from datetime import datetime

def track_habit1(habit_name, start_date):
  goal = 30
  time_elapsed = (datetime.now()-start_date)
  hours = (time_elapsed// 60 // 60, 1)
  days = round(hours // 24, 2)
  days_to_go = (goal-days)
  if hours > 72:
    hours = str(days) + 'days'
  else:
    hours = str(hours) + 'hours'
  return {'habit':habit_name, 'time since':time_elapsed, 'days remaining':days_to_go}

print(track_habit1('Coffee', datetime(2021,7,20,10,20)))

