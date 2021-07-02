<h2>5818. Longest Common Subsequence Between Sorted Arrays</h2><h3>Medium</h3><hr><div><p>Given an array of integer arrays <code>arrays</code> where each <code>arrays[i]</code> is sorted in <strong>strictly increasing</strong> order, return <em>an integer array representing the <strong>longest common subsequence</strong> between all the arrays</em>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> arrays = [[<u>1</u>,3,<u>4</u>],
&nbsp;              [<u>1</u>,<u>4</u>,7,9]]
<strong>Output:</strong> [1,4]
<strong>Explanation:</strong>&nbsp;The longest subsequence which in the two arrays is [1,4].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> arrays = [[<u>2</u>,<u>3</u>,<u>6</u>,8],
&nbsp;              [1,<u>2</u>,<u>3</u>,5,<u>6</u>,7,10],
&nbsp;              [<u>2</u>,<u>3</u>,4,<u>6</u>,9]]
<strong>Output:</strong> [2,3,6]
<strong>Explanation:</strong>&nbsp;The longest subsequence which in all of the three arrays is [2,3,6].
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> arrays = [[1,2,3,4,5],
&nbsp;              [6,7,8]]
<strong>Output:</strong> []
<strong>Explanation:</strong>&nbsp;There is no common subsequence between the two arrays.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arrays.length &lt;= 100</code></li>
	<li><code>1 &lt;= arrays[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= arrays[i][j] &lt;= 100</code></li>
	<li><code>arrays[i]</code> is sorted in strictly increasing order.</li>
</ul>
</div>