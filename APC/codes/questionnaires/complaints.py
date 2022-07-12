# complaints_index = int(input())
# percent_solved_complaints = int(input())
# percent_cancel_request = int(input())
# availability_index = int(input())
# problems_cancel = int(input())


def complaints(
    complaints_index,
    percent_solved_complaints,
    percent_cancel_request,
    availability_index,
    problems_cancel,
):

    complaint_dissatisfaction_index = complaints_index

    if percent_solved_complaints >= 60:
        complaint_dissatisfaction_index -= 5
    elif percent_solved_complaints < 60:
        complaint_dissatisfaction_index += 15

    print(complaint_dissatisfaction_index)

    if percent_cancel_request >= 10:
        if problems_cancel:
            complaint_dissatisfaction_index += 80
        elif not problems_cancel:
            complaint_dissatisfaction_index -= 30
    elif percent_cancel_request < 10:
        if problems_cancel:
            complaint_dissatisfaction_index += 50
        elif not problems_cancel:
            complaint_dissatisfaction_index -= 10

    print(complaint_dissatisfaction_index)

    if availability_index >= 10:
        complaint_dissatisfaction_index += 70
    elif availability_index < 10:
        complaint_dissatisfaction_index -= 20

    print(complaint_dissatisfaction_index)
