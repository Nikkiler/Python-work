def task(numMarks,num_list):
    total = 0
    for count in range(numMarks):
        total = total + num_list[count]
    if 3 in num_list:
        return 'None'
    else:
        avg = total / numMarks
        if avg == 3.0:
            return 'None'
        elif avg == 5.0:
            return 'Named'
        elif avg >= 4.5:
            return 'High'
        else:
            return 'Common'

def run_manually():
    #input 1
    numExams = int(input())
    #input 2
    numList = []
    for count in range(numExams):
        mark = int(input())
        numList.append(mark)
    result = task(numExams, numList)
    print(result)

def run_pre_defined(numExams, list, expected_result):
    result = task(numExams, list)
    print(result)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def run_tests():
    # comment test cases which are not needed
    run_pre_defined(3, [5, 5, 4], 'High')
    run_pre_defined(3, [3, 3, 3], 'None')
if __name__ == '__main__':
    # uncomment line below to run manually
    run_manually()
    #run_tests()