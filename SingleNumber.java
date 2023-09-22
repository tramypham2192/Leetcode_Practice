class Solution {
    public int singleNumber(int[] nums) {
        //step 1: declare a new hash map
        //step 2: iterate through the nums array. if the hash map containsKey a nums[i], 
        //declare a new variable, named frequence = hashmap.get(nums[i]) + 1. if not contain, 
        //set frequence = 1
        
        //iterate through the hash map. if there is frequence = 1, print out the getKey()
        
        int result = 0;
        HashMap<Integer, Integer> hmap = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++){
            if (hmap.containsKey(nums[i])){
                int frequence = hmap.get(nums[i]);
                hmap.put(nums[i], frequence + 1);
            } else {
                hmap.put(nums[i], 1);
            }
        }
        
        for (Map.Entry<Integer, Integer> traverseMap : hmap.entrySet()){
            if (traverseMap.getValue() == 1){
                result = traverseMap.getKey();
            }
        }
        return result;
    }
}
