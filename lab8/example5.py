#Password Checker

def passw_check(password):
  level = 0
  if len(password) < 8 or " " in password:
    level = 0
  else:
    if password.isalpha() == True:
      level += 1
      if password.isnumeric() == True:
        level += 1
        if password.isalnum() == True:
          level += 1
  return level

def main():
  password = input("Enter a password: ")
  print("Security level",passw_check(password))

main()