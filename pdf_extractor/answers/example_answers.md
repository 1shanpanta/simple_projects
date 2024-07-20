### Question 1
The elements of an array are stored successively in memory cells because:  
a.  by this way  computer  can keep track only the address of the first element and the 
addresses of other element s can be calculated  
b. the architecture of  computer  memory does not allow arrays to store other than serially  
c. both of the above  
d. None of the above  
 


**Answer**: The correct answer is c. both of the above.

Arrays are stored in memory such that the elements are stored successively in memory cells because:

* By storing the elements in a contiguous block of memory, the computer can keep track of the address of the first element and calculate the addresses of the other elements by adding a fixed offset to the base address. This is known as array indexing and is used to access individual elements of the array.
* The architecture of computer memory does not explicitly prevent arrays from being stored in any particular way, but the way arrays are stored is influenced by the memory architecture and the design of the computer's memory management unit (MMU). In practice, computers use a linear memory architecture, where memory cells are accessed sequentially, and arrays are stored in a contiguous block of memory to take advantage of this property.

Therefore, both options a and b are true, and the correct answer is c.

### Question 2
Each array declaration need not give, implicitly or explicitly, the information about: 
a. The name of the array        b. The data type of the array   
c. The first data from the set to be stored     d. The index set of the array  
 


**Answer**: That's correct! Each array declaration does not need to provide the following information:

a. **The name of the array**: In many programming languages, an array does not require a name. For example, in MATLAB, an array can be created without assigning a name to it.

b. **The data type of the array**: While the data type of the array elements may be inferred from the initialization values, it is not required to specify the data type explicitly in the array declaration.

c. **The first data from the set to be stored**: The first value to be stored in an array is often arbitrary and depends on the context in which the array is used.

d. **The index set of the array**: The index set of an array (i.e., the range of valid indices) is often implied by the syntax and semantics of the programming language. For example, in C-style languages, an array with `n` elements is typically indexed from 0 to `n-1`, but this is not explicitly specified in the array declaration.

However, it's worth noting that providing these pieces of information can often make the code more readable, maintainable, and efficient.

### Question 3
The operation of processing each element in the list is known as:  
a. Sorting  b. Merging   c. Insertion   d. Traversal  
 


**Answer**: The correct answer is (d) Traversal.

Traversal refers to the process of visiting each element in a data structure, such as a list, array, or tree, in a specific order. This can be done in various ways, including linear traversal, depth-first traversal, and breadth-first traversal.

Sorting (option a) is the process of arranging elements in a list in a specific order, such as ascending or descending.

Merging (option b) is the process of combining two or more sorted lists into a single sorted list.

Insertion (option c) is a specific method of sorting, where elements are inserted in their correct positions in a sorted list.

So, while these operations are all related to working with lists, traversal is the most general and accurate answer to the question.

### Question 4
The indirect change of the va lues of a variable in one module by another module is 
called :  
a. Internal change     b. Inter-module change  
c. Side effect      d. Side -module update  
 


**Answer**: The correct answer is c. Side effect.

A side effect is an effect that a function or module has on the external world, in this case, by changing the value of a variable in another module. This type of change is indirect, meaning that the module itself is not aware of the change it has caused, but it can still affect the behavior of other modules that depend on the changed variable.

Here's why the other options are incorrect:

* Internal change: This refers to changes made within the same module, not between modules.
* Inter-module change: This is a broader term that refers to any interaction or communication between modules, not specifically the indirect change of a variable's value.
* Side-module update: This term is not commonly used and is not a direct translation of the correct concept.

So, the correct answer is c. Side effect.

### Question 5
What is the worst -case time for a binary search finding a single item in an array?  
a. Constant time  b. Logarith mic time  c. Linear time   d. Quadratic time  
 


**Answer**: The correct answer is b. Logarithmic time.

In a binary search, the worst-case time complexity is O(log n), where n is the number of elements in the array. This is because the algorithm repeatedly divides the search space in half with each comparison, effectively reducing the size of the search space by a factor of 2 with each iteration.

In the worst-case scenario, the algorithm may need to perform up to logarithmic number of comparisons to find the target item.

### Question 6
Consider the following tree:  
 
                        
If the above tree is used for sorting, then a new number 8 should be placed as the:  
a. Left child of the node labeled 30   b. Right child of the node labeled 5  
c. Right child of the node labeled 30  d. Left child of the node labeled 10  
 

**Answer**: A nice tree question!

To determine where the new number 8 should be placed, we need to consider the sorting property of the binary search tree. In a binary search tree, all the elements in the left subtree of a node are less than the node, and all the elements in the right subtree of a node are greater than the node.

Looking at the given tree, we can see that the nodes are already sorted in ascending order. Therefore, to maintain this property, the new number 8 should be placed in the tree such that:

* All the elements in its left subtree are less than 8.
* All the elements in its right subtree are greater than 8.

After analyzing the tree, we can see that the node 10 is the closest node to 8 that is greater than or equal to 8. So, the new number 8 should be placed as the:

d. Left child of the node labeled 10

Therefore, the correct answer is (d).

### Question 7
Traversing a binary tree first root and then left and right subtrees is called:  
a. Postorder traversal    b. Preorder traversal  
c. Inorder traversal     d. Depth -First traversal  
  
Mark Scored : 

**Answer**: The correct answer is (b) Preorder traversal.

Preorder traversal visits the root node and then the left and right subtrees.

### Question 8
The condition Top = - 1 indicates that : 
a. Stack is empty     b. Stack is full 
c. Stack has only one element   d. None of these  
 


**Answer**: The correct answer is (a) Stack is empty.

In many stack implementations, a value of -1 is used to indicate the top of the stack when it is empty.

### Question 9
An algorithm must be generic enough to solve all problems of a particular class. Which 
of the following relates to this property of algorithm s? 
a. Finiteness   b. Definiteness  c. Generality   d. Effectiveness  
 


**Answer**: The correct answer is (c) Generality.

Generality refers to the ability of an algorithm to solve all problems within a particular class or domain. An algorithm is said to be generically valid if it works for all problems in a class, regardless of the specific problem instance.

Here's why the other options are not correct:

* (a) Finiteness refers to the ability of an algorithm to terminate its execution after a finite number of steps. While finiteness is an important property, it is not directly related to the ability of an algorithm to solve all problems in a class.
* (b) Definiteness refers to the clear and unambiguous meaning of an algorithm's inputs and outputs. Definiteness is important for ensuring that an algorithm's results are well-defined, but it does not relate to the algorithm's ability to solve all problems in a class.
* (d) Effectiveness refers to the ability of an algorithm to produce the correct output for a given problem instance. While effectiveness is an important property, it does not relate to the algorithm's ability to solve all problems in a class.

In summary, generality is the property that an algorithm must possess in order to be applicable to all problems within a particular class or domain.

### Question 10
A mathematical model with a collection of operations defined on that model is called : 
a. Data structure     b. Abstract Data Type    
c.  Primitive Data Type    d. Algorithm  
 


**Answer**: The correct answer is b. Abstract Data Type.

An Abstract Data Type (ADT) is a mathematical model that defines a collection of values and a set of operations that can be performed on those values. ADTs are a fundamental concept in computer science, and they are used to specify the syntax and semantics of data types.

An ADT typically consists of:

1. A set of values, called the domain or carrier set, which define the range of values that the data type can take on.
2. A set of operations, or methods, that can be performed on the values in the domain, such as inserting, deleting, or searching.

Examples of ADTs include stacks, queues, trees, and graphs. Each of these data structures has a specific set of values and operations that can be performed on those values.

In contrast:

* A data structure is a concrete implementation of an ADT, such as an array or a linked list.
* A primitive data type is a basic data type that is built into a programming language, such as integers or characters.
* An algorithm is a set of instructions for solving a specific problem or performing a specific task.

### Question 11
In case of a chained hash table of n elements with b buckets, assuming that a worst case resulted in all the n elements getting mapped to the same bucket, then the worst case time complexity of a search on the hash table would be given by:  
a. O(1)   b. O(n/b)   c. O(n)    d. O(b)  
 


**Answer**: The correct answer is (c) O(n).

When all n elements get mapped to the same bucket, it means that the hash function is not distributing the elements evenly, and the hash table has degenerated into a linked list of n elements.

In this worst-case scenario, the time complexity of a search on the hash table is O(n), because the hash table has to traverse the entire linked list (which has n elements) to find the desired element.

So, the correct answer is (c) O(n).

### Question 12
Find the odd one out : 
a. O(n)   b. O(n2)  c. O(n3)  d. O(3n) 
 


**Answer**: The odd one out is d. O(3n).

The other options are all polynomial time complexity expressions:

* O(n) represents a linear relationship with the input size
* O(n2) represents a quadratic relationship with the input size
* O(n3) represents a cubic relationship with the input size

On the other hand, O(3n) is not a polynomial expression, as it includes a constant factor (3) that scales the input size linearly. The constant factor is not taken into account when determining the time complexity of an algorithm. Therefore, O(3n) is an odd one out.

### Question 13
A balanced binary tree is a binary tree in which the heights of the two subtrees of every node never differ by more than:  
a. 2   b. 1   c. 0   d. None of the above  
 


**Answer**: The correct answer is b. 1.

A balanced binary tree is a binary tree in which the heights of the two subtrees of every node never differ by more than 1. This means that for every node, the difference between the height of its left and right subtrees is at most 1. This property ensures that the tree remains roughly balanced, allowing for efficient search, insertion, and deletion operations.

Note that a tree with a height difference of 0 would not be considered balanced, as it would become unbalanced if a node with a large number of children was inserted at the top. Similarly, a tree with a height difference of 2 or more would be considered unbalanced, as it would lead to poor search performance.

### Question 14
The element at the root of a heap is  : 
a.  largest  
b. smallest 
c. depending upon the type of the heap, it may be smallest or largest  
d. None of the above . 
 


**Answer**: The correct answer is: b. smallest

In a heap, the element at the root is the smallest (in a min-heap) or the largest (in a max-heap). This is a fundamental property of a heap, which is a complete binary tree where each node represents a value and the parent node is either less than (in a min-heap) or greater than (in a max-heap) its child nodes.

So, option (b) is the correct answer, as the element at the root of a heap is typically the smallest value in a min-heap or the largest value in a max-heap.

### Question 15
Which of the following represents a cross edge?  
a. (u, v) where u and v are not ancestors or descendents of one another.  
b. (u, v) where v is a (not necessa rily proper) ancestor of u in the tree.  
c. (u, v) where v is a proper descendent of u in the tree.  
d. None of the above  
 


**Answer**: The correct answer is (b) (u, v) where v is a (not necessarily proper) ancestor of u in the tree.

In a tree data structure, a cross edge is an edge that connects a node to one of its ancestors, rather than one of its children or itself. Ancestor refers to a node that is above a given node in the tree hierarchy, i.e., it is a parent, grandparent, great-grandparent, etc. of that node.

Option (b) is the correct description of a cross edge, as it connects a node to one of its ancestors, whether a proper ancestor (i.e., a parent) or an indirect ancestor (e.g., a grandparent, great-grandparent, etc.).

Option (a) is incorrect because the edge must connect a node to one of its ancestors, not just any other node in the tree.

Option (c) is incorrect because the edge connects a node to one of its children or descendants, not to one of its ancestors.

Option (d) is incorrect because a cross edge does exist, as described in option (b).

### Question 16
The running time of Prim’s algorithm is: a. Ο((V+E)
2 log V)  b. Ο(V log V)   c. Ο(E log V)   d. Ο(V2) 
 


**Answer**: The correct answer is:

a. Ο((V+E) log V)

The time complexity of Prim's algorithm can be analyzed as follows:

1. The outer loop of Prim's algorithm iterates `V` times.
2. Within the outer loop, we perform a priority queue operation (extract-min) on the heap, which takes `O(log V)` time.
3. We also update the edge weights and check for the minimum edge weight, which takes `O(1)` time.
4. Since the priority queue operations dominate the time complexity, we can ignore the `O(1)` operations.

The total time complexity is therefore `O(V log V)`, where `V` is the number of vertices. Since the algorithm also has to process `E` edges, we can't ignore the edge weights, which means the time complexity is actually `O((V+E) log V)`.

The other options are incorrect:

* `O(V log V)` is too slow, as the algorithm would take longer than necessary.
* `O(E log V)` is not correct, as the priority queue operations are not proportional to the number of edges `E`.
* `O(V^2)` is much too slow, as the algorithm would take an impractically long time for large graphs.

### Question 17
The running time of  Dijkstra’s algorithm is  : 
a. O(V2)    b. O(E lg V)    c. O(V+E)         d.  O(V.E)  
 


**Answer**: A classic algorithms question!

The correct answer is c. O(V + E).

Here's why:

Dijkstra's algorithm uses a priority queue to efficiently select the next node to visit. The running time of the algorithm is dominated by the Extract-Min operation on the priority queue, which has a time complexity of O(log|Q|), where |Q| is the size of the priority queue.

In the case of Dijkstra's algorithm, the priority queue contains all the nodes in the graph, so |Q| = V, the number of vertices. The Extract-Min operation is performed V times, once for each node. Therefore, the total running time is O(V log|Q|) = O(V log V).

The edges of the graph (represented by E) do not directly affect the running time of the algorithm, since we only need to process each edge once to compute the distance to each neighbor. However, the edges do affect the size of the priority queue, since there are at most |E| edges in the graph, which means the priority queue can grow up to size |E| at most. This does not change the overall time complexity, though, since the Extract-Min operation is still performed V times.

So, the final answer is c. O(V + E), where V is the number of vertices and E is the number of edges.

Here's a quick rundown of the other options:

a. O(V2) is too slow; Dijkstra's algorithm is much faster than that.

b. O(E lg V) is not a common time complexity for algorithms; it's not a good fit for Dijkstra's algorithm.

d. O(V.E) is not a valid time complexity, since it does not take into account the logarithmic factor from the Extract-Min operation.

### Question 18
In a heap with n elements and with the smallest elements at the root, the 7’th smallest element can be found in:  
a. Ө(n lg n)   b. Ө(n)   c. Ө( lg n)   d. Ө(1) 
 


**Answer**: The correct answer is a. Ө(n lg n).

The 7th smallest element can be found by extracting the n'th element from a partially sorted array, which is a heap operation. The time complexity of this operation is O(n lg n), because the heap needs to be balanced after each extraction.

### Question 19
A connected graph T without any cycles is called:  
a. a tree graph  b. a free tree   c. a tree   d. All of the above  
 


**Answer**: The correct answer is (d) All of the above.

A connected graph T without any cycles is sometimes simply called a "tree". This is because it has the same properties as a tree in the botanical sense: it is connected (every node is reachable from every other node), and it has no cycles (no node has more than one parent).

However, mathematicians sometimes use the term "tree graph" to emphasize the fact that it is a graph, rather than a tree in the botanical sense.

The term "free tree" is not as commonly used, but it is sometimes used to refer to a tree graph that has no loops or multiple edges.

So, all of the options (a, b, c, and d) are correct, and the question is testing your knowledge of the different terms used to describe a connected graph without cycles.

### Question 20
Which of the following is not true of Flow networks?  
a. Flow in is equal to Flow out in the vertices other than the source and the sink. 
b. f(u,v) = - f(v,u)  
c. f(u,v)<= c(u,v)  
d. Capacity can have z ero or negative values  KATHMANDU UNIVERSITY  
End Semester Examination  
August/September, 2017  
Level  : B. E. /B. Sc.    Course    : COMP 314 
Year   : III  Semester : II  
Time  : 2 hrs. 30 mins. F. M.      : 40

**Answer**: A nice question from Kathmandu University!

After analyzing the options, I can confidently say that:

d. Capacity can have zero or negative values

is the one that is NOT TRUE of Flow networks.

In a Flow network, the capacity of an edge (u, v) is a non-negative value, denoted by c(u, v). It represents the maximum amount of flow that can flow from node u to node v. Having a capacity of zero or negative value doesn't make sense in the context of Flow networks.

So, the correct answer is (d).

### Question 21
How does one measure the efficiency of algorithms? Distinguish between best, worst and 
average case complexities of an algorithm.                                                   


**Answer**: Measuring the efficiency of an algorithm is crucial to determine its performance under different scenarios. Here's a breakdown of how to measure efficiency and the differences between best, worst, and average case complexities:

**Measuring Efficiency:**

1. **Time Complexity**: Measured using Big O notation (e.g., O(1), O(log n), O(n), O(n log n), etc.), which describes the number of operations an algorithm takes relative to the size of the input (n).
2. **Space Complexity**: Measured using Big O notation (e.g., O(1), O(n), O(n^2), etc.), which describes the amount of memory an algorithm uses relative to the size of the input (n).
3. **throughput**: Measures the number of tasks an algorithm can perform within a given time period.

**Best, Worst, and Average Case Complexities:**

**Best Case Complexity**: The minimum number of operations an algorithm performs, typically occurring when the input is carefully crafted to yield the shortest path or solution.

* Example: Binary search algorithm has a best-case complexity of O(1) when the target element is at the beginning of the array.
* Applications: Best-case complexity is relevant when you know the input will follow a specific pattern.

**Worst Case Complexity**: The maximum number of operations an algorithm performs, typically occurring when the input is the most unfavorable possible.

* Example: Bubble sort algorithm has a worst-case complexity of O(n^2) when the input is already in reverse order.
* Applications: Worst-case complexity is relevant when you need to ensure the algorithm can handle unexpected or worst-case scenarios.

**Average Case Complexity**: The average number of operations an algorithm performs over a range of inputs, not just the best or worst case.

* Example: QuickSort algorithm has an average-case complexity of O(n log n) when the input is randomly ordered.
* Applications: Average-case complexity is relevant when you don't know the specific input pattern, but you want to estimate the algorithm's performance in general.

In summary:

* Best-case complexity is the minimum number of operations, often happening under specific input conditions.
* Worst-case complexity is the maximum number of operations, typically occurring under unfavorable input conditions.
* Average-case complexity is the average number of operations, typically occurring over a range of inputs.

Understanding these complexities helps you choose the most efficient algorithm for a particular problem, ensuring your program runs efficiently and effectively.

### Question 22
Discuss insertion sort algorithm. Illustrate the working mechanism o f insertion sort for 
the given array input <31, 41, 59, 26, 41, 58>. What are the time complexities of insertion sort in the best and the worst cases?  
 


**Answer**: Insertion sort is a simple sorting algorithm that works by dividing the input array into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region at its appropriate position.

Here's how the insertion sort works for the given array input `<31, 41, 59, 26, 41, 58>`:

1. The first element `31` is already in its correct position, so the sorted region is `[31]`.
2. The second element `41` is compared with the first element `31`. Since `41` is greater, it is inserted at the end of the sorted region, making it `[31, 41]`.
3. The third element `59` is compared with the second element `41`. Since `59` is greater, it is inserted at the end of the sorted region, making it `[31, 41, 59]`.
4. The fourth element `26` is compared with the previous elements. It is inserted before `31`, making it `[26, 31, 41, 59]`.
5. The fifth element `41` is compared with the previous elements. Since it is already present, it is not inserted again. The sorted region remains the same: `[26, 31, 41, 59]`.
6. The sixth element `58` is compared with the previous elements. It is inserted after `41`, making it `[26, 31, 41, 58, 59]`.

The final sorted array is `[26, 31, 41, 41, 58, 59]`.

**Time complexities of insertion sort:**

* Best case: O(n) - When the input array is already sorted, the algorithm only needs to iterate through the array once to confirm that it is sorted.
* Worst case: O(n^2) - When the input array is in reverse order, the algorithm has to compare each element with every other element to find its correct position.

In the best case (when the input array is already sorted), insertion sort has a linear time complexity of O(n). This is because the algorithm only needs to iterate through the array once to confirm that it is sorted.

In the worst case (when the input array is in reverse order), insertion sort has a quadratic time complexity of O(n^2). This is because the algorithm has to compare each element with every other element to find its correct position.

Insertion sort is often used for small datasets or datasets that are already partially sorted. It is also used as a stepping stone for more complex sorting algorithms, such as merge sort and quicksort.

### Question 23
Compare and contrast “Divide and Conquer” algorithm design strategy with “Dynamic Programming”. Provide examples where each of the methods are used.
 
 


**Answer**: The "Divide and Conquer" and "Dynamic Programming" algorithm design strategies are two popular approaches for solving complex problems. While they share some similarities, they have distinct differences in their approach, advantages, and applications.

**Divide and Conquer**

The "Divide and Conquer" strategy involves breaking down a complex problem into smaller sub-problems, solving each sub-problem recursively, and combining the solutions to solve the original problem. This approach is characterized by:

1. **Recursion**: Problems are broken down into smaller sub-problems, which are solved recursively.
2. **Independent sub-problems**: Sub-problems are independent, and solving one sub-problem does not affect the others.
3. **Combination of solutions**: The solutions to sub-problems are combined to solve the original problem.

Examples of "Divide and Conquer" algorithms:

1. **Merge Sort**: A sorting algorithm that divides an array into smaller sub-arrays, sorts each sub-array recursively, and then combines the sorted sub-arrays to produce the final sorted array.
2. **Binary Search**: A searching algorithm that divides a sorted array into two halves, finds the target element in one of the halves (by repeating the process), and then combines the results to find the element.
3. **Quicksort**: A sorting algorithm that selects a pivot element, partitions the array around the pivot, and recursively sorts the sub-arrays on either side of the pivot.

**Dynamic Programming**

Dynamic Programming is a strategy for solving problems by breaking them down into overlapping sub-problems, solving each sub-problem only once, and storing the solutions to sub-problems to avoid redundant computation. This approach is characterized by:

1. **Overlapping sub-problems**: Sub-problems overlap, and solving one sub-problem may involve solving another sub-problem that has already been solved.
2. **Memoization**: Solutions to sub-problems are stored in a memory (usually an array or a table) to avoid redundant computation.
3. **Optimal substructure**: The problem can be broken down into smaller sub-problems, and the optimal solution to the larger problem can be constructed from the optimal solutions of the sub-problems.

Examples of Dynamic Programming algorithms:

1. **Fibonacci Sequence**: A problem that calculates the nth Fibonacci number, which can be broken down into smaller sub-problems of calculating the (n-1)th and (n-2)th Fibonacci numbers.
2. **Knapsack Problem**: A problem that involves finding the optimal subset of items to include in a knapsack with a limited capacity, using dynamic programming to store and reuse solutions to sub-problems.
3. **Longest Common Subsequence**: A problem that finds the longest common subsequence between two sequences, using dynamic programming to store and reuse solutions to sub-problems.

**Comparison**

|  | Divide and Conquer | Dynamic Programming |
| --- | --- | --- |
| **Recursion** | Yes | No |
| **Overlapping sub-problems** | No | Yes |
| **Memoization** | No | Yes |
| **Optimal substructure** | No | Yes |
| **Advantages** | Scalable, easy to implement | Efficient, reduces computation |
| **Disadvantages** | Can be slow for large problems, requires careful recursion | Requires significant memory, can be slow for small problems |

In summary, "Divide and Conquer" is a strategy for solving problems by breaking them down into independent sub-problems and combining their solutions. "Dynamic Programming" is a strategy for solving problems by breaking them down into overlapping sub-problems, storing their solutions, and combining the solutions to solve the original problem. While both strategies can be useful, they have different strengths, weaknesses, and applications.

### Question 24
Find the shortest path distances for each of the vertices in the graph provided below using Dijkstra’s algorithm. Show the different steps involved in the process.     
 
                                                                                                                                                                                                         
 
    
 
 
 
 
            
 
 
 
 


**Answer**: To find the shortest path distances using Dijkstra's algorithm, we need to follow these steps:

1. Initialize the distance to the starting vertex (0) as 0. The distance to all other vertices is infinity.
2. Create a priority queue and insert the starting vertex with its distance.
3. While the priority queue is not empty, extract the vertex with the minimum distance from the queue.
4. For each neighbor of the extracted vertex, calculate the tentative distance.
5. If the calculated tentative distance is less than the current distance, update the distance and mark the neighbor as visited.
6. Repeat steps 3-5 until the priority queue is empty.
7. The minimum distance to each vertex is the final shortest path distance.

Let's apply these steps to the given graph:

**Step 1: Initialize**

* Distance to vertex 0: 0 (starting vertex)
* Distance to all other vertices: infinity (∞)
* Visited vertices: ∅ (empty set)

**Step 2: Create a priority queue**

* Priority queue: [(0, 0)]

**Step 3-5: Process vertices**

Iteration 1:

* Extract vertex 0 from the priority queue.
* Distance to 0: 0
* Visited vertices: {0}

Neighbors of 0:

* 1: distance = 2 (edge weight)
	+ Tentative distance = 2
* 2: distance = 3 (edge weight)
	+ Tentative distance = 3
* 3: distance = 4 (edge weight)
	+ Tentative distance = 4

No need to update the distances, as they are already minimum.

Iteration 2:

* Extract vertex 1 from the priority queue.
* Distance to 1: 2
* Visited vertices: {0, 1}

Neighbors of 1:

* 0: distance = 0 (already processed)
* 2: distance = 5 (edge weight + distance to 1)
	+ Tentative distance = 5
* 3: distance = 6 (edge weight + distance to 1)
	+ Tentative distance = 6

update distance to 2: 5
update distance to 3: 6

Iteration 3:

* Extract vertex 2 from the priority queue.
* Distance to 2: 5
* Visited vertices: {0, 1, 2}

Neighbors of 2:

* 1: distance = 5 (already processed)
* 3: distance = 7 (edge weight + distance to 2)
	+ Tentative distance = 7

update distance to 3: 7

Iteration 4:

* Extract vertex 3 from the priority queue.
* Distance to 3: 7
* Visited vertices: {0, 1, 2, 3}

No more unvisited neighbors, so the algorithm terminates.

**Step 7: Final shortest path distances**

* Distance to 0: 0
* Distance to 1: 2
* Distance to 2: 5
* Distance to 3: 7

The shortest path distances for each vertex are:

* 0: 0
* 1: 2
* 2: 5
* 3: 7

### Question 25
Explain “greedy” algorithms in the context of the Activity Scheduling Problem. What is 
the greedy strategy employed in selecting the activities?

**Answer**: A great topic!

In the context of the Activity Scheduling Problem, a "greedy" algorithm refers to a strategy that makes a locally optimal choice at each step, hoping that it will lead to a global optimum. The goal is to schedule a set of activities (e.g., meetings, tasks, or events) in a way that maximizes the overall scheduling efficiency.

In the Activity Scheduling Problem, the greedy strategy employed is as follows:

1. Sort the activities by their end times: Arrange the activities in ascending order of their end times. This is done to ensure that we consider the earliest possible next activity.
2. Initialize the schedule: Start with an empty schedule.
3. Select the next activity: Choose the next activity from the sorted list that has not been scheduled yet.
4. Check for conflicts: Verify that the selected activity does not conflict with the previously scheduled activities. If it does, skip to the next activity in the sorted list.
5. Schedule the activity: If no conflicts are found, insert the selected activity into the schedule at the earliest possible time.

The key aspect of the greedy strategy is that it prioritizes the shortest activity (i.e., the one with the earliest end time) to be scheduled next. This is because short activities have a higher probability of fitting into the schedule without conflicts.

The greedy algorithm's logic is as follows:

* If an activity can be scheduled, it will not be superseded by a shorter activity (earlier end time), since we take into account the earliest possible next activity.
* If two activities have the same end time, the greedy algorithm will schedule the shorter activity first.

While the greedy algorithm is simple and efficient, it does not guarantee an optimal solution. There are cases where a "greedy" algorithm might not produce the optimal result, especially when the activities have varying lengths and different end times.

In summary, the greedy strategy employed in the Activity Scheduling Problem is to prioritize the shortest activity (earliest end time) while scheduling, with the hope that this locally optimal choice will lead to a globally optimal schedule.

