from project import add_data,delete_data,update_data

def test_create():
    add_data("data.csv", "example.com", "user123", "password123")

    add_data("data.csv", "example2.com", "user1234", "password")



def test_delete():
    delete_data("data.csv", "example.com")

    delete_data("data.csv", "nonexistent.com")



def test_update():

    update_data("data.csv", "example.com")

    update_data("data.csv", "nonexistent.com")




def test_view():

    pass


if __name__ == "__main__":
    test_create()
    test_delete()
    test_update()
    test_view()
