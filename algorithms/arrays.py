class ArrayUtils:
    #Return the second largest number from a list.
    def second_largest(self,numbers):
        numbers = [int(x) for x in numbers.split(",")]
        max1 = max2 = float('-inf')
        for n in numbers:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2 and n!= max1:
                max2 = n

        if max2 == float('-inf'):
            return None
        return(max2)
    #Remove duplicates from list while preserving order.
    def duplicate_removal(self,list_input):
        list_input = [x.strip() for x in list_input.split(",")]
        unique_list = []
        for i in list_input:
            if i not in unique_list:
                unique_list.append(i) 
        return(unique_list)
    #Find missing number from range 1..n.
    def missing_number(self, numbers):
        numbers = [int(n) for n in numbers.split(",")]
        numbers_sum = sum(numbers)
        n = max(numbers)
        expected_sum = n * (n + 1) // 2
        if expected_sum != numbers_sum:
            return expected_sum - numbers_sum
        return None
