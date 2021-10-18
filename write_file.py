character_read = open("main_character.txt", mode='w')

character_read.write('Yato Yagami\n')

print('Raku Ichijou', file=character_read)

more_main_characters = ['Senku Ishigami\n', 'Izuku Midoriya\n']

character_read.writelines(more_main_characters)

character_read.close()
