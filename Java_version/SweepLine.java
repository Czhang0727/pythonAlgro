// Sweep Line solution for question 
// http://www.lintcode.com/en/problem/number-of-airplanes-in-the-sky/

/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */
//segment tree????
class Solution {
    /**
     * @param intervals: An interval array
     * @return: Count of airplanes are in the sky.
     */
    public int countOfAirplanes(List<Interval> airplanes) { 
        //pq for saving incoming interval;
        
        // write your code here
        int max = 0;
        if (airplanes == null || airplanes.size() == 0){
            return max;
        }
        PriorityQueue <Interval> pq = new PriorityQueue<Interval>(airplanes.size(),
            new  Comparator<Interval>(){
                @Override
                public int compare(Interval o1, Interval o2){
                    if (o1.end == o2.end){
                        return o1.start - o2.start;
                    }
                    return o1.end - o2.end;
                }
            });
        Collections.sort(airplanes, new  Comparator<Interval>(){
                @Override
                public int compare(Interval o1, Interval o2){
                    if (o1.start == o2.start){
                        return o1.end - o2.end;
                    }
                    return o1.start - o2.start;
                }
            });
            
        while(!airplanes.isEmpty()){
            Interval top = airplanes.get(0);
            airplanes.remove(0);
            while(pq.size() > 0 && pq.peek().end <= top.start){
                //if(pq.peek().end <= Top.start){
                    pq.poll();
                //}
            }
            pq.add(top);
            max = Math.max(max, pq.size());
        }
        return max;
    }
}

//Another solution might be segment tree, or interval tree. 
