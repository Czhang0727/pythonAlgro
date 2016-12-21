import java.lang.*;

class unionFind{
    private int[] father;
    public unionFind(Object [] arr){
        this.father = new int[arr.length];
    }
    public int find(int val){
        if(father[val] != 0){
            father[val] = find(father[val]);
        }
        return father[val];
    }
    public void union(int a, int b){
        int root_a = find(a);
        int root_b = find(b);
        if (root_a != root_b){
            father[root_a] = root_b;
        }
    }




}