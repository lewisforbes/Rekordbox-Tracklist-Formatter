f = open('tracklist_raw.txt', 'r')
output = ""
first_line = True
for l in f:
  if first_line:
    first_line = False
    continue
  l = l.split("	")
  output += "{} - {}\n".format(l[2], l[3].replace("/", ", "))

output = output[:len(output)-1]
f.close()
f = open('formatted_tracklist.txt', 'w')
f.write(output)
f.close()
print(output)