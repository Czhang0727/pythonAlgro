public class Solution {
    /**
     * @param board: A list of lists of character
     * @param words: A list of string
     * @return: A list of string
     */
     
     TierTree root;
    public ArrayList<String> wordSearchII(char[][] board, ArrayList<String> words) {
        // write your code here
        boolean [][] cheese = new boolean[board.length][board[0].length];
        buildTierTree(words);
        ArrayList<String> res = new ArrayList<String>();
        for (int i = 0; i < board.length; ++i){
            for (int j = 0; j < board[0].length; ++j){
                find(board, root, i,j, res, cheese);
            }
        }
        return res;
    }
    
    void buildTierTree(ArrayList<String> words){
        root = new TierTree();
        for (String word : words){
            addWord(word);
        }
    }
    
    void find(char[][]board, TierTree root, int x, int y, ArrayList<String> res, boolean [][] cheese){
        if (root == null){
            return ;
        }
        if(root.isLeaf){
            res.add(root.full);
            // here to avoid duplicate
            root.isLeaf = false;
        }

        if (cheese[x][y]){
            return ;
        }
        char p = board[x][y];
        // if exist
        
        if (root.children[p - 'a'] != null){
            cheese[x][y] = true;
            if(x > 0){
                find(board, root.children[p-'a'], x-1, y, res, cheese);
            }
            if(y > 0){
                find(board, root.children[p-'a'], x, y - 1, res, cheese);
            }
            if(x < board.length - 1){
                find(board, root.children[p-'a'], x + 1, y, res, cheese);
            }
            if(y < board[0].length - 1){
                find(board, root.children[p-'a'], x, y + 1, res, cheese);
            }
            cheese[x][y] = false;
        }
        return;
    }
    
    public void addWord(String word) {
        TierTree tmp = root;
        for (int i = 0; i < word.length(); ++i){
            char q = word.charAt(i);
            if(tmp.children[q - 'a'] == null){
                tmp.children[q - 'a'] = new TierTree();
            }
            tmp = tmp.children[q - 'a'];
        }
        tmp.isLeaf = true;
        tmp.full = word;
    }
    
    class TierTree{
        TierTree [] children;
        boolean isLeaf;
        String full;
        public TierTree(){
            children = new TierTree[26];
            isLeaf = false;
        }
    }
}
