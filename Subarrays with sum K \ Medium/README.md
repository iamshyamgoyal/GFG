<h2><a href="https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/">Subarrays with sum K</a></h2> <h3>Difficulty Level : Medium</h3> <hr> <div class="problems_problem_content__Xm_eO"> 
<p><span style="font-size: 18px;">Given an unsorted array of integers, find the number of continuous subarrays having a sum exactly equal to a given number <code>k</code>.</span></p> 
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p> 
<pre><span style="font-size: 18px;"> <strong>Input:</strong> arr = [10, 2, -2, -20, 10], k = -10 
<strong>Output:</strong> 3 <strong>
Explanation:</strong> The subarrays with a sum of -10 are: 1. [10, 2, -2, -20] (from index 0 to 3) 2. [2, -2, -20, 10] (from index 1 to 4) 3. [-20, 10] (from index 3 to 4) </span></pre> <pre><span style="font-size: 18px;"> 
<strong>Input:</strong> arr = [9, 4, 20, 3, 10, 5], k = 33 
<strong>Output:</strong> 2 <strong>
Explanation:</strong> The subarrays with a sum of 33 are: 1. [9, 4, 20] (from index 0 to 2) 2. [20, 3, 10] (from index 2 to 4) </span></pre> 
<pre><span style="font-size: 18px;"> 
<strong>Input:</strong> arr = [1, 3, 5], k = 0 
<strong>Output:</strong> 0 
<strong>Explanation:</strong> There are no subarrays with a sum of 0. </span></pre> <p><span style="font-size: 18px;">
<strong>Constraints:</strong></span></p> <ul style="font-size: 18px;"> <li>1 ≤ arr.size() ≤ 10<sup>5</sup></li> <li>-10<sup>3</sup> ≤ arr[i] ≤ 10<sup>3</sup></li> <li>-10<sup>7</sup> ≤ k ≤ 10<sup>7</sup></li> </ul> <p><span style="font-size: 18px;">
<strong>Topic Tags :</strong><br><code>Hash</code>&nbsp;&nbsp;<code>Data Structures</code>&nbsp;</span></p>
