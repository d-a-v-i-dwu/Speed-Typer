# alist = ["a", "b", "c"]
# b = alist.index("f")
# print(b)

import random

list = [1, 2, 3, 4, 5]

random.shuffle(list)

print(list)

"0123456789"
print(random.randrange(8,9))

explanations = [("Fran", "You're a witty, funny, and interesting individual who has a gravity that attracts those around you.\n\nYou likely give off the impression of having a simple life, but are still somehow a constant stream of\ndelightful surprises even to people who'd like to think they know you well.\n\nYou have many admirable talents and skills, and are projected to have a wonderful year ahead.\n\nBut, alas, there is one personality that's better."), ("David", "Well done, you got the best one."), ("Fred", "Work is the number one thing in your life, and you flaunt that fact unapolagetically.\n\nYou were raised rich and are now a pretentious, slimy asshole, whether you realize it or not.\n\nYou're probably a little creepy around younger girls, but your type is still mature women\n(minimum 10yrs hospo experience)."), ("Peanut", "You're the type of person to call chasing after women a form of art, even though it's one you're not\nparticularly good at.\n\nYou enjoy writing not because it's a means of catharsis, but rather because you see it as a tool to impress people.\n\nYou have a tendency to do cringe things that are painful even just to hear about, and your excuses\ninvolve either alcohol or your" +  ' "mates."'), ("Yarrick", "You're potentially a tad racist and misogynistic, traits which are inherited from your\nmother who is the central figure in your life\n\nYou likely have one ancient friend who you reference non-stop and who you reminisce about daily, even though\nhe hasn't talked to nor though of you since you parted ways five years ago.\n\nYou like putting on an air of superiority around people you're older than, despite\nyou having arguably fewer life achievements and prospects.")]
for ele in explanations:
    print(ele[1])