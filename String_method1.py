a = "sayan"
print(a)
upp= a.upper()  #strings are immutable
doww = upp.lower()
print(upp)
print(doww)
strip_ex = "!!sayan!!!"
r_strip1 = strip_ex.rstrip("!")
print(r_strip1)
l_strip1 = strip_ex.lstrip("!")
print(l_strip1)
replace_ex = "!!!!Sayan!!!!!!!!Sayan!!!!!"
replaced_ex = replace_ex.replace("Sayan", "john")
print(replaced_ex)
#split- convert string to lists
sent = "I am going to school"
l1 = sent.split(" ")
print(l1)
# count function
cex = sent.count("o")
print(cex)
#endswith() function give true or false
print(sent.endswith("hool"))
# find() funcction find and returns the index of the specified thing if not found returns -1
#isalnum() returns if string is alphanumeric
#isalpha() returns if string is A-Z, a-z.
#islower() returns true if string lower case
#isprintable returns true false
#istitle()
#swapcase()
#startswith()
# title()
