'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if not "th" in word:
        return 0
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[2:])
    else:
        return + count_th(word[2:])

        
print(count_th("this test"))
print(count_th("tis test"))
print(count_th("this testh"))


# ```
# c)  def bunnyEars(bunnies):
#       if bunnies == 0:
#         return 0

#       return 2 + bunnyEars(bunnies-1)
# ```

# def count_th(word):

#     if not "th" in word:
#         return f"false"
#     else:
#         return 

        
# print(count_th("this test"))
# print(count_th("tis test"))