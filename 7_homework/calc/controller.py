import model
import view
def button_click():
    numbers = view.get_numbers()
    f_name = view.fraction_name()
    operation = view.get_operation()
    value_a=view.get_value()
    value_b=view.get_value()
    model.init(value_a,value_b)

    result = model.sum()
    view.view_data(result)