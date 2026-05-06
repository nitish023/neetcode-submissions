class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val == ".":
                    continue
                if int(val) in check:
                    return False
                check.add(int(val))
             
            check.clear()
   
        col = 0
        while col < len(board):
            for row in range(len(board)):
                val = board[row][col]
                if val == ".":
                    continue
                if int(val) in check:
                    return False
                check.add(int(val))
            check.clear()
            col += 1

        check_dict = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                r_index, c_index = row // 3, col // 3
                val = board[row][col]
                if val == ".":
                    continue
                
                if int(val) in check_dict[(r_index, c_index)]:
                    return False
               
                check_dict[(r_index, c_index)].add(int(val))
    
        return True


        
            
                