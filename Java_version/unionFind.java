import java.lang.*;

public class unionFind { 

    int [] father;
    public unionFind(int n) {
        // initialize your data structure here.
        father = new int[n + 1];
    }
    private int find(int x){
        if (father[x] != 0){
            int q = find(father[x]);
            father[x] = q;
            return q;
        }
        return x;
        
    }

    public void union(int a, int b) {
        // Write your code here
        if (!query(a, b)){
            father[find(a)] = find(b);
        }
    }
        
    public boolean query(int a, int b) {
        // Write your code here
        return find(a) == find(b);
    }
}
