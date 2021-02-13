


vt = ["a", "b", "c"]
vn = ["S", "B", "C", "D"]

grammar = {
  "S":[("a", "B")], 
  "B":[("b", "S"),("a", "C"),("b", None)],
  "C":[("b", "D")],
  "D":[("a", None),("b", "C"),("c", "S")],
}

isAnswerFound = False

def printPath(path):
  for vertexIndex in range(len(path)):
    if vertexIndex == len(path) - 1:
      print(path[vertexIndex])
      return
    print(path[vertexIndex], end=" -> ")

def FiniteAutomata(startVertex, visited, path, generatedWord, inputWord):
  global isAnswerFound 

  visited[startVertex]= True
  path.append(startVertex) 

  for adjacencyTuple in grammar[startVertex]: 
    if generatedWord + adjacencyTuple[0] == inputWord and adjacencyTuple[1] == None:
      printPath(path)
      isAnswerFound = True
      return

    if len(generatedWord) > len(inputWord) or adjacencyTuple[1] == None:
      continue

    FiniteAutomata(adjacencyTuple[1], visited, path, generatedWord + adjacencyTuple[0], inputWord) 

  generatedWord = ""                
  path.pop() 
  visited[startVertex]= False

   
def main(): 
  print("Write a string to check if it is valid for the given grammar")

  inputWord = str(input()) 

  areTerminalSymbolsValid = all(char in vt for char in inputWord)
  
  if not areTerminalSymbolsValid:
    print("The given string contains invalid terminal symbols")
    return

  visited = {"S":False,"B":False,"C":False,"D":False}
  
  FiniteAutomata("S", visited, [], '', inputWord)

  if not isAnswerFound:
    print("The given string is not valid for current grammar")


main()