
import PySimpleGUI as sg
import random

panel=["","","","","","","","",""]
winner=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
layout = [
  [sg.Button("  ",key="0"),sg.Button("  ",key="1"),sg.Button("  ",key="2")],
  [sg.Button("  ",key="3"),sg.Button("  ",key="4"),sg.Button("  ",key="5")],
  [sg.Button("  ",key="6"),sg.Button("  ",key="7"),sg.Button("  ",key="8")],
  [sg.Text("",key="TEXT")]]

def judge():
  for a,b,c in winner:
    if panel[a]==panel[b] and panel[b]==panel[c]:
      if panel[a]=="0": window["TEXT"].update("You win"); return
      if panel[a]=="X": window["TEXT"].update("You lose"); return

window = sg.Window("",layout)
while True:
  event, values = window.read()
  if event==None: break
  panel[int(event)] = "0"
  window[event].update(text="0")
  judge()
  for pc in range(9):
    if panel[pc]=="":
      panel[pc] = "X"
      break;
  else: window["TEXT"].update("Draw")
  window[str(pc)].update(text="X")
  judge()
