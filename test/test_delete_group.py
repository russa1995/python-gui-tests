from random import randrange

def test_delete_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    index = randrange(len(old_list))
    app.groups.delete_group(index)
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    old_list[index:index+1] = []
    assert sorted(old_list) == sorted(new_list)