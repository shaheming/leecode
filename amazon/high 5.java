public class Solution{
	public List<List<Integer>> highFive(int renderCount, List renderTimeOfPage){
		Map<Integer, Double> average = new HashMap<>();
		Map<Integer, PriorityQueue<Integer>> times = new HashMap;

		for (PageRenderTime x: renderTimeOfPage){
			int page = x.pageID;
			int time = x.renderTime;
			if (!times.containsKey(page)) times.put(page, new PriorityQueue<>());
			times.get(page).add(time);
			if (times.get(page).size()>5)
				times.get(page).poll();

		}

		// for (Map.Entry<Integer, PriorityQueue<Integer>> item: times.entrySet()){
		// 	double s = 0.0;
		// 	Queue<Integer> time = item.getValue();
		// 	while (!time.isEmpty())
		// 		s += time.poll();
		// 	average.put(item.getKey(), sum/5)
		// }

		int [][] res = new int[times.size()][2];
		int i = 0;
		for (Map.Entry<Integer, PriorityQueue<Integer>> item: times.entrySet()){
			double s = 0.0;
			Queue<Integer> time = item.getValue();
			while (!time.isEmpty())
				s += time.poll();
			res[i][0] = item.getKey();
			res[i][1] = sum/5;
			i++;
		}
		return res;
	}
}