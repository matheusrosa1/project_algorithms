def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for entry_time, exit_time in permanence_period:
            if entry_time <= target_time <= exit_time:
                counter += 1
        return counter
    except TypeError:
        return None
