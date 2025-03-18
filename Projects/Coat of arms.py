###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("spring")

q1=codesters.Square(100, 100, 200, 'blue')
q2=codesters.Square(-100, 100, 200, 'yellow')
q3=codesters.Square(-100, -100, 200, 'red')
q4=codesters.Square(100, -100, 200, 'green')

s1=codesters.Sprite("Cash", 100, 100)
s1.set_size(0.3)
s2=codesters.Sprite("abc", -100, -100)
s2.set_size(0.3)
s3=codesters.Sprite("def", 100, -100)
s3.set_size(0.8)
s4=codesters.Sprite("sign", -100, 100)
s4.set_size(0.6)

message1 = codesters.Text("My name is Cash", 0 , 220, "black")
message2 = codesters.Text("I like money", 0 ,-220, "black")