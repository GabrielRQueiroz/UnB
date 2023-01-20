study_plans = int(input())


def study_organizer(subjects, schedule=["m", "e", "n"]):
    # schedule is respectively divided in morning, evening and night
    # subjects is the string with the subjects to study
    subjects = sorted(subjects)
    schedule = sorted("".join(schedule))

    if schedule == subjects:
        return "It's in the box!"
    elif len(schedule) > len(subjects):
        return "You died!"
    else:
        for scheduled_subject in [*schedule]:
            if scheduled_subject in subjects:
                subjects.remove(scheduled_subject)
                schedule.remove(scheduled_subject)
            else:
                return "You died!"

        extra_subjects = set([subject for subject in subjects])

        return f"Bora ralar: {''.join(sorted(extra_subjects))}"


for _ in range(study_plans):
    subjects = input().upper()
    morning_schedule = input().upper()
    evening_schedule = input().upper()
    night_schedule = input().upper()

    print(study_organizer(subjects, [morning_schedule, evening_schedule, night_schedule]))
