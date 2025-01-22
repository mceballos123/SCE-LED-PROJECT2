from sqllite_helper import create_table,add_user,update_user,display_all_user,top_user,get_first_place,delete_user

def test_db():
    db_file='leetcode.db'
    create_table(db_file)

    display_all_user(db_file)
    top_user(db_file)
    get_first_place(db_file)
    

if __name__ =='__main__':
    test_db()