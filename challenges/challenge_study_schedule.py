def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for entry_time, exit_time in permanence_period:
            if entry_time <= target_time <= exit_time:
                counter += 1
        return counter
    except TypeError:
        return None


"""     try:
        return sum(
            entry_time <= target_time <= exit_time
            for entry_time, exit_time in permanence_period
        )
    except TypeError:
        return None """

""" permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 5
print(study_schedule(permanence_period, target_time))
 """
