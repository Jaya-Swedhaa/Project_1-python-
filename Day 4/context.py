import sqlite3

create= 'CREATE TABLE IF NOT EXIST jjj (fname TEXT lname Text)'
insert= "INSERT INTO jjj VALUES ('jaya','r'),('swedh','s')"
select= 'SELECT*FROM jjj'

def main():
    db_path=':memory:'

    c = sqlite3.connect(db_path)
    a = c.cursor()

    try:
        a.execute(create)
        c.commit()

        a.execute(insert)
        c.commit()

        a.execute(select)

        print(a.fetchall())

    except Exception as e:
        print("The try was failed")

    finally:
        c.close()

if __name__ =='__main':
    main()