public class WordDictionary {

    TrieTree root;
    public WordDictionary(){
        root = new TrieTree();
    }
    // Adds a word into the data structure.
    public void addWord(String word) {
        TrieTree tmp = root;
        for (int i = 0; i < word.length(); ++i){
            char q = word.charAt(i);
            if(tmp.children[q - 'a'] == null){
                tmp.children[q - 'a'] = new TrieTree();
            }
            tmp = tmp.children[q - 'a'];
        }
        tmp.isLeaf = true;
        // Write your code here
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return find(root, word, 0);
        // Write your code here
    }
    
    boolean find(TrieTree root, String word, int pos){
        if (root == null)
            return false;
        if(pos >= word.length()){
            return root.isLeaf;
        }
        char p = word.charAt(pos);
        if (p == '.'){
            for (TrieTree node : root.children){
                if(find(node, word, pos + 1)){
                    return true;
                }
            }
            return false;
        }
        return find(root.children[p-'a'], word, pos + 1);
    }
    class TrieTree{
        TrieTree [] children;
        
        boolean isLeaf;
        String full;
        public TrieTree(){
            children = new TrieTree[26];
            isLeaf = false;
            
        }
    }
}
