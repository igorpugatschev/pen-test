# Легкий способ выучить Python 3 еще глубже — страница 80

ОДНОСВЯЗНЫЕ СПИСКИ 79
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
assert colors.count() == 2
assert colors.pop () = "Cadmium Orange"
assert colors.count() = 1
assert colors.pop() == "Carbazole Violet"
assert colors.count () == 0
def test_remove():
colors = SingleLinkedList()
colors.push("Cobalt")
colors.push("Zinc White")
colors.push("Nickle Yellow")
colors.push("Perinone")
assert colors.remove("Cobalt") == 0
colors.dump("before perinone")
assert colors.remove("Perinone") == 2
colors.dump("after perinone")
assert colors.remove("Nickle Yellow") == 1
assert colors.remove("Zinc White") == 0
def test first () :
colors = SingleLinkedList()
colors.push("Cadmium Red Light")
assert colors .first () = "Cadmium Red Light"
colors.push("Hansa Yellow")
assert colors .first () == "Cadmium Red Light"
colors.shift("Pthalo Green")
assert colors .first () = "Pthalo Green"
def test—last():
colors = SingleLinkedList()
colors.push("Cadmium Red Light")
assert colors.last() = "Cadmium Red Light"
colors.push("Hansa Yellow")
assert colors.last() = "Hansa Yellow"
colors.shift("Pthalo Green")
assert colors.last() = "Hansa Yellow"
def test—get():
colors = SingleLinkedList()
colors.push("Vermillion")
assert colors.get (0) == "Vermillion"
colors.push("Sap Green")
