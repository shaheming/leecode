class Solution{
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K){
        Map<Integer, Map<Integer, Integer>> prices = new HashMap<>();
        for (int [] f: flights){
            if(!prices.containsKey(f[0])) prices.put(f[0], new HashMap<>());
            prices.get(f[0]).put(f[1],f[2]);
        }
        
        PriorityQueue<int []> pq = new PriorityQueue<>((a,b) -> (Integer.compare(a[0], b[0])));
        pq.offer(new int[] {0, src, K+1});
        while (!pq.isEmpty()){
            int[] top = pq.poll();
            int price = top[0];
            int city = top[1];
            int stop = top[2];
            if (city == dst) return price;
            if (stop > 0){
                Map<Integer, Integer> adj = prices.getOrDefault(city, new HashMap());
                for(int a: adj.keySet()){
                    pq.offer(new int[] {price+adj.get(a), a, stop-1});
                }
            }
        }
        return -1;
    }
}



// class Solution {
//     public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
//         int[][] dist = new int[2][n];
//         int INF = Integer.MAX_VALUE/2;
//         Arrays.fill(dist[0], INF);
//         Arrays.fill(dist[1], INF);
//         dist[0][src] = dist[1][src] = 0;
        
//         for(int i = 0; i <= K; i++){
//             for (int[] edge: flights){
//                 dist[i&1][edge[1]] = Math.min(dist[i&1][edge[1]], dist[~i&1][edge[0]]+edge[2]);
//             }
//         }
//         return dist[K&1][dst] < INF ? dist[K&1][dst] : -1;
//     }
// }