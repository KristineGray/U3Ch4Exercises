# 4.10. Exercises: Data & Variables

# Part A, #1 :
print('Part A, #1:')
print(6 * (1 - 2)) #Result should be -6

# Part A, #2 here:
print('\nPart A, #2:')
print((2 + 8 + 10) / 5) #Result should be 4.0
print(2 + (8 + 10) / 5) #Result should be 5.6

# Part A, #3 here:
word = 'word'

#3A
print('\nPart A, #3a:')
print((word + ' ') * 4)

#3B
print('\nPart A, #3b:')
print((word*2 + '\n')*3)

#3C
print('\nPart A, #3c:')
print((((word + '\t') * 3) + '\n') * 3)

print('<----------------------------------------->')
print('\nPart B:')

# 1. Declare and assign your first 4 variables here:
ship_name = 'Determination'
ship_speed_mph = 17500
km_to_mars = 225000000
miles_per_km = 0.621

print("\nName: " + ship_name +
      ", \nspeed(mph): " + str(ship_speed_mph) +
      ", \nkm to Mars: " + str(km_to_mars) +
      ", \nmiles per km: " + str(miles_per_km))
# 2. Create and assign a miles to Mars variable here:
miles_to_mars = km_to_mars * miles_per_km
print("\nMiles to Mars:", miles_to_mars)
      
# 3 & 4. Calculate and store the hours it takes to get to Mars
# and the days to Mars:
hours_to_mars = miles_to_mars / ship_speed_mph
print("\nHours to Mars:", hours_to_mars)

# 5. Print the sentence, "_____ will take ___ days to reach Mars."
#Fill in the blanks with the spaceship name and the calculated time.
print()
print(ship_name, "will take", miles_to_mars / 24, "days to reach Mars.")

# 6. Code the bonus mission here:
print('\nPart B, Bonus Mission:')
km_to_moon = 384400
miles_to_moon = km_to_moon * miles_per_km
hours_to_moon = miles_to_moon / ship_speed_mph
days_to_moon = hours_to_moon / 24
print()
print(ship_name, "will take", days_to_moon, "days to reach the Moon.")

print('<----------------------------------------->')

print('\nPart C, #1:')
word_input = input('Enter a word: ')
word_length = len(word_input)
print("The word '" + word_input + "' contains " + str(word_length) + " characters.")

print('\nPart C, #2:')
rectangle_length = float(input('Enter a length: '))
rectangle_width = float(input('Enter a width: '))
rectangle_area = rectangle_length * rectangle_width
print("The rectangle has an area of " + str(rectangle_area) + ".")

print('\nPart C, #3:')
miles_driven = float(input('Enter the number of miles driven: '))
gallons_used = float(input('Enter the number of gallons used: '))
miles_per_gal = miles_driven / gallons_used
print('Your car got', miles_per_gal, 'miles per gallon.')
