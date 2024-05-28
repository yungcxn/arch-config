bf = r"""     
.==-.                   .-==.
 \()8`-._  `.   .'  _.-'8()/
 (88"   ::.  \./  .::   "88)
  \_.'`-::::.(#).::::-'`._/
    `._... .q(_)p. ..._.'
      ""-..-'|=|`-..-""
      .""' .'|=|`. `"".
    ,':8(o)./|=|\.(o)8:`.
   (O :8 ::/ \_/ \:: 8: O)
    \O `::/       \::' O/
     ""--'         `--""
"""

begin_body = [
  (3,12),
  (4,14),
  (5,14),
  (6,14),
  (7,14),
  (8,14),
  (9,14),
  (10,14)
]

end_body = [
  (3,19),
  (4,17),
  (5,17),
  (6,17),
  (7,17),
  (8,17),
  (9,17),
  (10,17),
  (11,15),
  (12,15),
  (2,16)
]

c = "\u001b["
reset = c + "0m"
black = c+"30m"
red = c+"31m"
green = c+"32m"
yellow = c+"33m"
blue = c+"34m"
magenta = c+"35m"
cyan = c+"36m"
lgray = c+"37m"
dgray = c+"90m"
lred = c+"91m"
lgreen = c+"92m"
lyellow = c+"93m"
lblue = c+"94m"
lmagenta = c+"95m"
lcyan = c+"96m"
white = c+"97m"

bold = c+"1m"

target = bf
b = ""
x,y = (1,1)
for li in target.split("\n"):
  for l in li:
    if x == 1:
      b += cyan + bold + " " * 2
    if (y,x) in begin_body:
      b += green + bold
    if (y,x) in end_body:
      b += magenta + bold
    b += l
    x+=1
  b += "\n"
  y+=1
  x = 1


with open("bf_color.txt", "w") as t:
    t.write(b)
    t.close()

