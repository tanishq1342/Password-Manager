import sqlite3
import string
import random

conn = sqlite3.connect('password.db')

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS passwordTable(password BLOB, username BLOB, website TEXT UNIQUE)')

# c.execute('DROP TABLE IF EXISTS passwordTable')

def resetPassword(new_password, website):
    c.execute('UPDATE passwordTable SET password = ? WHERE website = ?', (new_password, website))
    conn.commit()

def store(password, username, website):
    # c.execute("""CREATE TABLE password(
    #             password blob,
    #             website text,
    #             )""")
    try:
        c.execute("INSERT INTO passwordTable(password, username, website) VALUES(?, ?, ?)",
              (password, username, website))

        conn.commit()
    except Exception as e:
        print("Website's password already exists try show command to see")

def show():
    c.execute(f'SELECT * FROM passwordTable')
    for row in c.fetchall():
        print(row)

def delete(website):
    sql = 'DELETE FROM passwordTable WHERE website=?'
    cur = conn.cursor()
    cur.execute(sql, (website,))
    conn.commit()

whatToDo = input("What to do Store Password(store), generate password(generate) or show password(show) or delete password(delete) or reset password (reset)? :").lower()


if whatToDo == "generate":
    if __name__ == "__main__":
        passwordLength = input("Enter password length: \n")
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        newPassLength = int(passwordLength)
        s = []
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)    
        random.shuffle(s)
        newPassword = "".join(s[0:newPassLength])
        print(newPassword)
    storeOrNot = input("Do you want me to store it (Y/N)? ")
    if storeOrNot == "Y":
        website = input("Enter name of website: \n")
        usernameToStoreAfterGen = input("Enter username: \n")
        store(newPassword, usernameToStoreAfterGen, website)
    elif storeOrNot == "N":
        pass

elif whatToDo == "store":
    passwordToStore = input("Enter password: \n")
    websiteToStore = input("Enter website: \n")
    usernameToStore = input("Enter username: \n")
    store(passwordToStore, usernameToStore, websiteToStore)

elif whatToDo == "show":
    passwordForEncryptedDatabase = "blabla"
    passwordEncrypted = input("Enter password: \n")
    if passwordEncrypted == passwordForEncryptedDatabase:
        show()
    else:
        print("wrong password")

elif whatToDo == "delete":
    websiteToDelete = input("Enter website for which password needs to be deleted: \n")
    delete(websiteToDelete)

elif whatToDo == "reset":
    websiteToReset = input("Enter website for which password needs to be reset: \n")
    ResetedPassword = input("Enter new password: \n")
    resetPassword(websiteToReset, ResetedPassword)

else:
    print('Invalid Option!!')
