/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function(nums, target) {
    let newArr = []
    if (nums.length < 2){
        return
    }
    else {
        for (var i=0; i < nums.length; i++){
            for (var j= i+1; j < nums.length; j++){
                if (nums[i] + nums[j] === target){
                    newArr.push(i,j)
                    return newArr
                }
            }
        }
    }
};


