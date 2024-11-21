class ScheduleExporter:
    @staticmethod
    def export_to_html(schedule, year, month):
        html_schedule = f"""
        <html>
        <head>
            <title>Care Schedule for {calendar.month_name[month]} {year}</title>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 10px;
                    text-align: center;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>Care Schedule for {calendar.month_name[month]} {year}</h1>
            <table>
                <tr>
                    <th>Mon</th>
                    <th>Tue</th>
                    <th>Wed</th>
                    <th>Thu</th>
                    <th>Fri</th>
                    <th>Sat</th>
                    <th>Sun</th>
                </tr>
        """
        first_weekday, num_days = calendar.monthrange(year, month)
        current_day = 1
        for week in range((num_days + first_weekday) // 7 + 1):
            html_schedule += "<tr>"
            for day in range(7):
                if (week == 0 and day < first_weekday) or current_day > num_days:
                    html_schedule += "<td></td>"
                else:
                    shifts = schedule.get(current_day, {"AM": "Unassigned", "PM": "Unassigned"})
                    html_schedule += f"<td>{current_day}<br><b>AM:</b> {shifts['AM']}<br><b>PM:</b> {shifts['PM']}</td>"
                    current_day += 1
            html_schedule += "</tr>"
        html_schedule += "</table></body></html>"

        with open(f"care_schedule_{year}_{month}.html", "w") as file:
            file.write(html_schedule)
        print(f"Schedule exported to care_schedule_{year}_{month}.html")
