class Solution:
    def check_maps(self, arr1, arr2):
        # stores the final result
        result = []
        # A copy of arr2 but only to store the a, and b attributes of each object
        arr1_copy = []
        # Go through all objects in arr1 and store only the a and b attributes in arr_obj
        for arr in arr1:
            arr1_copy.append({'a':arr.get('a'), 'b':arr.get('b')})

        # Finallly go through each obj in arr2 and for each obj, check if it is found in arr1_copy
        for obj in arr1_copy:
            if obj in arr2:
                result.append(obj)

        return result


sol = Solution()
arr1 = [{'a':1, 'b':'foo', 'c':'bar'}, {'a':2, 'b':'baz', 'c':'qux'}]
arr2 = [{'a':2, 'b':'baz'}, {'a':3, 'b':'quux'}, {'a':1, 'b':'foo'}]
print(sol.check_maps(arr1, arr2))

