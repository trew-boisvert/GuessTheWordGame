from game import guess_is_correct

def assert_equal(actual, expected, testname):
    if actual == expected:
        print('PASSED')
    else:
        print(f'FAILED {testname}: Expected {expected} but got {actual}')

assert_equal(guess_is_correct('b', 'blave'), True, 'Letter is in Word')

assert_equal(guess_is_correct('z', 'happy'), False, 'Letter is not in Word')
