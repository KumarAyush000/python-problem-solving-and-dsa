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
    # Find common elements between two lists.
    """
    def common_elements(self, user_input_list):
        parts = user_input_list.split("/")
        if len(parts) != 2:
            raise ValueError("Input must contain two lists separated by '/'")
        list1 = [x.strip() for x in parts[0].split(",")]
        list2 = [x.strip() for x in parts[1].split(",")]
        common = []
        for item in list1:
            if item in list2 and item not in common:
                common.append(item)
        return common
    """
    def common_elements(self, user_input_list):
        parts = user_input_list.split("/")
        if len(parts) != 2:
            raise ValueError("Invalid input format")
        list1 = {x.strip() for x in parts[0].split(",")}
        list2 = {x.strip() for x in parts[1].split(",")}
        return list(list1 & list2)
    # Even Odd Counter
    def even_odd_count(self, numbers):
        try:
            numbers = [int(n.strip()) for n in numbers.split(",")]
        except ValueError:
            raise ValueError("Invalid input format")
        even = {"even_count" : 0, "even_values": []}
        odd = {"odd_count" : 0, "odd_values": []}
        for n in numbers:
            if n % 2 == 0:
                even["even_count"] += 1
                even["even_values"].append(n)
            else:
                odd["odd_count"] += 1
                odd["odd_values"].append(n)
        return even, odd
    #Rotate list k times.
    def rotate_list_slicing(self,nums, k):
        try:
            nums = [int(n.strip()) for n in nums.split(",")]
            k = int(k)
        except ValueError:
            raise ValueError("Invalid input format.")
        n = len(nums)
        k %= n
        return nums[n-k:] + nums[:n-k] 
    """
    Working: Input : [1,2,3,4,5,6,7,8,9,10]
                     k = 4
             1) nums[10-4:] → nums[6:] → [7,8,9,10]
             2) nums[:6] → [1,2,3,4,5,6]
             3) [7,8,9,10] + [1,2,3,4,5,6] → [7,8,9,10,1,2,3,4,5,6] Final Output
    """

    
