def main():
    #write your code below this line
  strList = []
  while(True):
    inputStr = input()
    if(inputStr==""):
      break
    strList.append(inputStr)
  
  searchStr = input("Search for?")
  for i in range(len(strList)):
    if(searchStr == strList[i]):
      print("%s was found!"%searchStr)
      break
    elif(i==len(strList)-1):
      print(("%s was not found!"%searchStr))
if __name__ == '__main__':
    main()
