<h2><a href="https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1">Count Subarrays with XOR k</a></h2> 
<h3>Difficulty Level : Medium</h3> <hr> <div class="problems_problem_content__Xm_eO"> 
  <p><span style="font-size: 18px;">Given an array of integers <code>arr[]</code> and a number <code>k</code>, count the number of subarrays whose XOR of elements equals <code>k</code>.</span></p> 
  <p><span style="font-size: 18px;"><strong>Examples:</strong></span></p> 
  <pre><span style="font-size: 18px;"> 
    <strong>Input:</strong> arr = [4, 2, 2, 6, 4], k = 6 
    <strong>Output:</strong> 4 
    <strong>Explanation:</strong> The subarrays with XOR equal to 6 are: 1. [4, 2] (from index 0 to 1) 2. [4, 2, 2, 6, 4] (from index 0 to 4) 3. [2, 2, 6] (from index 1 to 3) 4. [6] (from index 3 to 3) </span></pre> 
  <pre><span style="font-size: 18px;"> 
    <strong>Input:</strong> arr = [5, 6, 7, 8, 9], k = 5 
    <strong>Output:</strong> 2 
    <strong>Explanation:</strong> The subarrays with XOR equal to 5 are: 1. [5] (from index 0 to 0) 2. [5, 6, 7, 8, 9] (from index 0 to 4) </span></pre> 
  <p><span style="font-size: 18px;">
    <strong>Constraints:</strong></span></p> <ul style="font-size: 18px;"> <li>1 ≤ arr.size() ≤ 10<sup>5</sup></li> <li>0 ≤ arr[i] ≤ 10<sup>5</sup></li> <li>0 ≤ k ≤ 10<sup>5</sup></li> </ul> 
  <p><span style="font-size: 18px;"><strong>Topic Tags :</strong><br><code>Map</code>&nbsp;<code>Arrays</code>&nbsp;</span></p>
