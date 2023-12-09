countries_friends = {"Ukraine", "Poland"}
countries_new_friends = {"Great Britain", "USA", "Poland"}

# Оператор | об'єднує дві множини. 
# Якщо є однакові елементи,
# то в новій множині дублікати будуть видалені
print(countries_friends | countries_new_friends)

# Оператор & повертає нову множину із значеннями,
# які належать одночасно обом множинам (перетин)
print(countries_friends & countries_new_friends)

# Оператор - повертає множину з елементами, 
# які є в першій множині, але немає в іншій (різниця)
print(countries_friends - countries_new_friends)