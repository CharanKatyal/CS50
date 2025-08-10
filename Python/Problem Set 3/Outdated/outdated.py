def main():
    months = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Date: ").strip()

        try:
            # Try MM/DD/YYYY format
            if '/' in date_str:
                month, day, year = map(int, date_str.split('/'))
                if not (1 <= month <= 12 and 1 <= day <= 31):
                    raise ValueError
            # Try Month Day, YYYY format
            elif ',' in date_str:
                parts = date_str.replace(',', '').split()
                if len(parts) != 3:
                    raise ValueError
                month_name, day_str, year_str = parts
                month = months.index(month_name) + 1
                day = int(day_str)
                year = int(year_str)
                if not (1 <= day <= 31):
                    raise ValueError
            else:
                raise ValueError

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
