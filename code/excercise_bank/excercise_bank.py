read_file = open('/home/ubuntuwanderer/local-repo/code/2nd-self-instruced-week/code/exercise_bank/excercise_bank.txt', 'r')
encrypted = read_file.read()
read_file.close()

print(encrypted)