import networkx as nx
import matplotlib.pyplot as plt

vt = []
vn = []

grammar = dict()

isAnswerFound = False

def parseGrammar():
  global vt, vn, grammar

  file = open("v21.txt", "r")
  fileContent = file.read()

  vn = (fileContent[fileContent.index("VN")+4:fileContent.index("\n")-2]).split(", ")
  vt = (fileContent[fileContent.index("VT")+4:fileContent.index("\n", fileContent.index("VT"))-2]).split(", ")

  grammarList = (fileContent[fileContent.index("P")+3:fileContent.index("\n", fileContent.index("P"))-1]).split(", ")

  for grammarRule in grammarList:
    grammarComponents = grammarRule.split(" - ")
    nextVertex = grammarComponents[1][1] if len(grammarComponents[1]) == 2 else None

    if grammarComponents[0] not in grammar:
      grammar[grammarComponents[0]] = []

    grammar[grammarComponents[0]].append((grammarComponents[1][0], nextVertex))

def showGraph():
  G = nx.DiGraph()
  node_labels = []
  
  for nonTerminalSymbol in vn:
    if grammar[nonTerminalSymbol]:
      for adjacencyTuple in grammar[nonTerminalSymbol]:
        vertex =  adjacencyTuple[1] if adjacencyTuple[1] != None else "$"

        node_labels.append(((nonTerminalSymbol, vertex), adjacencyTuple[0]))
        G.add_edge(nonTerminalSymbol, vertex)

  layout = nx.circular_layout(G)

  nx.draw(G, layout, with_labels=True, font_weight='bold', connectionstyle="arc3,rad=0.1")
  nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=dict(node_labels), label_pos=0.2)

  plt.show()

def printPath(path, word):
  for vertexIndex in range(len(path)):
    if vertexIndex == 0:
      print(path[vertexIndex], end=" -> ")
      continue

    print(word[0: vertexIndex] + path[vertexIndex], end=" -> ")

  print(word)


def FiniteAutomata(startVertex, visited, path, generatedWord, inputWord):
  global isAnswerFound 

  visited[startVertex]= True
  path.append(startVertex) 

  for adjacencyTuple in grammar[startVertex]: 
    if generatedWord + adjacencyTuple[0] == inputWord and adjacencyTuple[1] == None:
      printPath(path, inputWord)
      isAnswerFound = True
      return

    if len(generatedWord) > len(inputWord) or adjacencyTuple[1] == None:
      continue

    FiniteAutomata(adjacencyTuple[1], visited, path, generatedWord + adjacencyTuple[0], inputWord) 

  generatedWord = ""                
  path.pop() 
  visited[startVertex]= False

   
def main(): 
  parseGrammar()

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
    return
  
  showGraph()

main()