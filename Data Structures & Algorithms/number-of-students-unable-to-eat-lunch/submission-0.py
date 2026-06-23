class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        std=students
        sand=sandwiches

        while std:
            if sand[0] not in std:
                break
            if sand[0]==std[0]:
                sand.pop(0)
                std.pop(0)
            else:
                a=std.pop(0)
                std.append(a)
        return len(std)        






        