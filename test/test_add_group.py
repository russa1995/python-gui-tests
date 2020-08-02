def test_add_group(app):
    pass
    old_list = app.groups.get_group_list()
    app.groups.add_new_group("my group")
    new_list = app.groups.get_group_list()
    old_list.append("my group")
    assert sorted(old_list) == sorted(new_list)