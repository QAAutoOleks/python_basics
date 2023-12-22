def test_search_five(new_list_create):
    value_boolean = False
    for i in new_list_create.list_random:
        if i == 5:
            value_boolean = True
            break
    assert value_boolean == True