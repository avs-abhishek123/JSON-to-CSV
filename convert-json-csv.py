import pandas as pd
import json
import os

def collect_into_csv(fname):
    headerow = ["question", "answer", "definition", "process", "purpose"]
    with open(fname, encoding='utf-8') as inputfile:
        inputdic = json.load(inputfile)
    inputfile.close()
    qstnlist = inputdic["ques"]
    answrlist = inputdic["ans"]
    rowlist = []
    for qstn,qindex in enumerate(qstnlist):
        currow = [qstn]
        currow.append(answrlist[qindex])
        currow.append("0")
        currow.append("0")
        currow.append("0")
        rowlist.append(currow)
    df = pd.DataFrame(rowlist, columns=headerow)
    df.to_csv('qstnlabeldata.csv')

if __name__ == "__main__":
    tfp = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(tfp, "QAdata8feb22.json")
    collect_into_csv(tfp)