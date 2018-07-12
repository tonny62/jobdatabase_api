
def writelog(message):
    with open('log1', 'a', encoding='utf-8') as fout:
        fout.write(message+"\n")

