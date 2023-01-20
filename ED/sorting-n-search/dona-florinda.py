pretendants_amount = int(input())
pretendants_list = []

for _ in range(pretendants_amount):
    pretendant_name, pretendant_surname, height, weight = input().split()
    pretendants_list.append(
        {
            "name": f"{pretendant_name}",
            "surname": f"{pretendant_surname}",
            "height": int(height),
            "weight": int(weight),
        }
    )


florinda_sorted_list = sorted(
    pretendants_list,
    key=lambda pretendant: (
        abs(pretendant["height"] - 180),
        abs(pretendant["weight"] - 75) if pretendant["weight"] <= 75 else pretendant["weight"],
        pretendant["surname"],
        pretendant["name"],
    ),
)

for pretendant in florinda_sorted_list:
    print(f"{pretendant['surname']}, {pretendant['name']}")
