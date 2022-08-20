from copy import deepcopy

clock = {
    "M": [
        "08:00 - 08:55",
        "08:55 - 09:50",
        "10:00 - 10:55",
        "10:55 - 11:50",
        "12:00 - 12:55",
    ],
    "T": [
        "12:55 - 13:50",
        "14:00 - 14:55",
        "14:55 - 15:50",
        "16:00 - 16:55",
        "16:55 - 17:50",
        "18:00 - 18:55",
    ],
    "N": [
        "19:00 - 19:50",
        "19:50 - 20:40",
        "20:50 - 21:40",
        "21:40 - 22:30",
    ],
}

weekdays = {2: "Seg", 3: "Ter", 4: "Qua", 5: "Qui", 6: "Sex", 7: "Sab"}


def sigaa_schedule(class_schedule={}):
    while True:
        commands = input()
        if commands == "Hasta la vista, beibe!":
            return None

        elif commands == "?":
            break

        action, class_id, *time = commands.split()

        for current_time in time:
            for character in current_time:
                if character == "T" or character == "N" or character == "M":
                    shift = character
                    break

            days = current_time[: current_time.index(shift) :]
            hours = current_time[current_time.index(shift) + 1 :]

            flag = False

            if action == "+":
                for day in days.split()[0]:
                    if flag == True:
                        break

                    for hour in hours.split()[0]:
                        if class_schedule.get(day) == None:
                            class_schedule[day] = {shift: {hour: class_id}}

                        elif class_schedule[day].get(shift) == None:
                            class_schedule[day].update({shift: {hour: class_id}})

                        elif class_schedule[day][shift].get(hour) == None:
                            class_schedule[day][shift].update({hour: class_id})

                        else:
                            print(f"!({action} {class_id} {current_time})")
                            flag = True
                            break

            elif action == "-":
                for day in days.split()[0]:
                    if flag == True:
                        break

                    for hour in hours.split()[0]:
                        if (
                            class_schedule.get(day) == None
                            or class_schedule[day].get(shift) == None
                            or class_schedule[day][shift].get(hour) == None
                            or class_schedule[day][shift][hour] != class_id
                        ):
                            print(f"!({action} {class_id} {current_time})")
                            flag = True
                            break

                        else:
                            class_schedule[day][shift].pop(hour)

                            if len(class_schedule[day][shift]) == 0:
                                class_schedule[day].pop(shift)

                            if len(class_schedule[day]) == 0:
                                class_schedule.pop(day)

    for day in class_schedule:
        for shift in class_schedule[day]:
            class_schedule[day][shift] = dict(
                sorted(class_schedule[day][shift].items(), key=lambda hour: int(hour[0]))
            )

    return dict(sorted(class_schedule.items(), key=lambda day: int(day[0])))


def sigaa_schedule_print(previous_schedule={}):
    class_schedule = sigaa_schedule(previous_schedule)

    if class_schedule == None:
        return

    previous_schedule = deepcopy(class_schedule)

    table = [
        [
            "+---------------+",
            "----------+",
            "----------+",
            "----------+",
            "----------+",
            "----------+",
            "----------+",
        ],
        [
            "|               |",
            " Seg      |",
            " Ter      |",
            " Qua      |",
            " Qui      |",
            " Sex      |",
            " Sab      |",
        ],
        [
            "+---------------+",
            "----------+",
            "----------+",
            "----------+",
            "----------+",
            "----------+",
            "----------+",
        ],
    ]

    time_list = []

    for day in class_schedule:
        for shift in class_schedule[day]:
            for hours in class_schedule[day][shift]:
                if (
                    class_schedule[day].get(shift) != None
                    and time_list.count((shift, int(hours) - 1)) == 0
                ):
                    time_list.append((shift, int(hours) - 1))

    time_list.sort(key=lambda shift: ["MTN".index(letter) for letter in shift[0]])

    while True:
        if len(time_list) == 0:
            break

        row = []

        current_shift, current_hour = time_list[0][0], time_list[0][1]

        row.append(f"| {clock[current_shift][current_hour]} |")

        for day in range(2, 8):
            day = str(day)

            if class_schedule.get(day) == None:
                row.append(f"          |")

            else:
                shift = list(class_schedule[day].keys())[0]

                if len(class_schedule[day].get(shift)) == 0:
                    class_schedule[day].pop(shift)

                if len(class_schedule.get(day)) == 0:
                    class_schedule.pop(day)
                    row.append(f"          |")
                    continue

                for shift in class_schedule[day]:
                    if shift != current_shift:
                        row.append(f"          |")
                        break

                    if len(list(class_schedule[day][shift].keys())) == 0:
                        row.append(f"          |")
                        break

                    hour = int(list(class_schedule[day][shift].keys())[0])

                    if hour - 1 != current_hour:
                        row.append(f"          |")
                        break

                    else:
                        row.append(f" {class_schedule[day][shift][str(hour)]} |")
                        class_schedule[day][shift].pop(str(hour))
                        break

        time_list.pop(0)

        table.append(row)
        table.append(
            [
                "+---------------+",
                "----------+",
                "----------+",
                "----------+",
                "----------+",
                "----------+",
                "----------+",
            ]
        )

    for line in table:
        print(*line, sep="")

    return sigaa_schedule_print(previous_schedule)


sigaa_schedule_print()
