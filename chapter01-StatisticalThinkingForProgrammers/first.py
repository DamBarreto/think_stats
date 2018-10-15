import survey
#survey.WorkPath()
table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies ' + str(len(table.records)))