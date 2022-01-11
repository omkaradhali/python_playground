from datetime import datetime


def main():
    api_date = "20181226152230"
    report_date = datetime.strptime(
        convert_to_time(
            api_date
        ),
        "%Y/%m/%d %H:%M:%S",
    )

    user_start_date = datetime.strptime("12-26-2018", "%m-%d-%Y")
    user_end_date = datetime.strptime("12-31-2018", "%m-%d-%Y")

    print(report_date)
    print(user_start_date)
    print(user_end_date)

    print(user_start_date <= report_date <= user_end_date)


def convert_to_time(t):
    if len(t) == 14:
        return (
                t[:4]
                + "/"
                + t[4:6]
                + "/"
                + t[6:8]
                + " "
                + t[8:10]
                + ":"
                + t[10:12]
                + ":"
                + t[12:14]
        )
    elif len(t) == 8:
        return t[:4] + "/" + t[4:6] + "/" + t[6:8]
    else:
        return ""


if __name__ == "__main__":
    main()
