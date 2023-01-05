import add_to_txt_csv
import find
import view

def phone_book():
    menu = 0
    while menu != 4:
        menu = view.main_menu()
        match menu:
            case 1:
                phone_data = view.write_data()
                add_to_txt_csv.add_to_txt(phone_data)
                add_to_txt_csv.add_to_csv(phone_data)
            case 2:
                find.full_output()
            case 3:
                lastname = view.search_data()
                find.find_data(lastname)