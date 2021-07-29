def try_me(text):

  if text == "bullet":
      return "---------------------------X"
  elif text == "cannonball":
      return "OOO0000000000000000000000000"
  else:
      return "try again"


if __name__ == "__main__":
    print(try_me("bullet"))
