# Type until done or skip

while True:  # loop forever
    line = raw_input("Type anything, type 'done' to exit: ")
    if line == 'done':
        break  # transfers control out of the loop

    if line == 'skip':
        continue  # transfers control back to the while statement

    print 'You entered:', line

print 'Finished'

