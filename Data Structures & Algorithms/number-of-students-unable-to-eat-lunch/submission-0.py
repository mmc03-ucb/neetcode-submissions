class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)

        for i in range(len(sandwiches)):
            if count[sandwiches[i]] == 0:
                break
            count[sandwiches[i]] -= 1
        
        remaining = 0

        for c in count.values():
            remaining += c
        
        return remaining
