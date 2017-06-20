import randint

class DiceAnimal():
    dice1 = 0
    dice2 = 0
    total = 0

    def rolldice(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.total = self.dice1 + self.dice2

vic = DiceAnimal()
bob = DiceAnimal()

vic.rolldice()
bob.rolldice()

print "Vic rolled a ", vic.dice1, " and a  ", vic.dice2
print "Bob rolled a ", bob.dice1, " and a  ", bob.dice2

if vic.total > bob.total:
    print "Vic wins!"
elif bob.total < vic.total:
    print "Bob wins!"
else:
    print "Its A Draw!"
