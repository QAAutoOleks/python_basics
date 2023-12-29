def look_up_odd_numbers(given_list):
    return_list = []
    for i in given_list:
        if i % 2 == 0:
            return_list.append(i)
    return return_list


given_list = [5, 8, -20, 200, 6.3]
list_for_testing = look_up_odd_numbers(given_list)

def test_is_odd_in_list(list_for_testing):
    assert list_for_testing == [8, -20, 200]
    assert len(list_for_testing) == 3
    assert list_for_testing.count(5) == 0

test_is_odd_in_list(list_for_testing)
    