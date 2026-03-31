class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {


function hasDuplicate(arr) {
  const seen = {};
  for (const num of arr) {
    if ("123456789".includes(num)) {
      if (num in seen) return true;
      else seen[num] = true;
    }
  }
  return false;
}
    // i first check the rows
  for (const row of board) {
    if (hasDuplicate(row)) return false;
  }

  //  then i check the columns (this is the tricky part lol)
  //   first i create an array of all the columns, i'm using a nested loop cause it's limited to just 9 rows so it can't be too bad right?
  const columns = [];
  for (const row of board) {
    let i = 0;
    for (const num of row) {
      if (columns[i]) {
        columns[i].push(num);
        i++;
      } else {
        columns[i] = [num];
        i++;
      }
    }
  }

  //   now i check if there's a duplicate in any of the arrays

  for (const col of columns) {
    if (hasDuplicate(col)) return false;
  }
  // now i build the box too
  const boxes = [[], [], [], [], [], [], [], [], []];

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (j >= 0 && j <= 2) {
        if (i <= 2) {
          boxes[0].push(board[i][j]);
        } else if (i > 2 && i <= 5) {
          boxes[3].push(board[i][j]);
        } else if (i > 5) {
          boxes[6].push(board[i][j]);
        }
      } else if (j >= 3 && j <= 5) {
        if (i <= 2) {
          boxes[1].push(board[i][j]);
        } else if (i > 2 && i <= 5) {
          boxes[4].push(board[i][j]);
        } else if (i > 5) {
          boxes[7].push(board[i][j]);
        }
      } else if (j > 5) {
        if (i <= 2) {
          boxes[2].push(board[i][j]);
        } else if (i > 2 && i <= 5) {
          boxes[5].push(board[i][j]);
        } else if (i > 5) {
          boxes[8].push(board[i][j]);
        }
      }
    }
  }
  //   and i check or duplicates in the boxes

  for (const box of boxes) {
    if (hasDuplicate(box)) return false;
  }

  return true;
}
}
