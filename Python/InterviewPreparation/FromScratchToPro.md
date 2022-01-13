# Step By Step through a Problem
**Note:** 
    - *Keep in mind that the more you prepare and understand what you need to code, the better the whiteboard will go.*
    - *So never start a whiteboard interview not being sure of how things are going to work out. That is a recipe for disaster.* 

1. **Note details**
    - Note the key points at the top (e.g sorted array). 
    - Make sure you have all the details (datatypes, dirty inputs, perhaps edge cases)
    - Show how organized you are.

2. **Double check**
    - Inputs? 
    - Outputs?

3. **Value of the problem**
    - Do you have time and/or space etc.. What is the main goal?

4. ***Don't be annoying and ask too many questions.**

5. **Start with the naive/ brute force approach.** 
    - Tell the first thing that comes into mind. It shows that you’re able to think well and critically
    - You don't need to write this code, just speak about it.

6. **Tell them why this approach is not the best** 
    - (i.e. O(n^2) or higher, not readable, etc...)

7. **Walk through your more efficient approach**
    - Comment steps and see where you may be able to break things
    - Any repetition, bottlenecks like O(N^2), or unnecessary work? 
    - Did you use all the information the interviewer gave you? 
    - Bottleneck is the part of the code with the biggest Big O, focus on that. Sometimes this occurs with repeated work as well.

8. **Note down your algorithm**
    - Before you start coding, walk through your code and write down the steps you are going to follow.
    - Modularize your code from the very beginning. Break up your code into beautiful small pieces and add comments if you need to.

10. **Start actually writing your code**
    - A lot of interviewers ask questions that you won’t be able to fully answer on time. So think: What can I show in order to show that I can do this and I am better than other coders. 
    - Break things up in Functions (if you can’t remember a method, just make up a function and you will at least have it there. Write something, and start with the easy part)

11. **Think about error checks** 
    - How you can break this code. Never make assumptions about the input. 
    - Assume people are trying to break your code. How will you safeguard it? Always check for false inputs that you don’t want. 
    - *Here is a trick: Comment in the code, the checks that you want to do… write the function, then tell the interviewer that you would write tests now to make your function fail (but you won't need to actually write the tests)*

12. **Don’t use bad/confusing names like i and j. Write code that reads well.**

13. **Test your code**
    - Check for no params, 0, undefined, null, massive arrays, async code, etc… 
    - Ask the interviewer if we can make assumption about the code. Can you make the answer return an error? Poke holes into your solution. Are you repeating yourself?

14. **Finally talk to the interviewer where you would improve the code**
    - Does it work? 
    - Are there different approaches? Is it readable? What would you google to improve? How can performance be improved? 
    - Possibly: Ask the interviewer what was the most interesting solution you have seen to this problem

15. **If your interviewer is happy with the solution, the interview usually ends here**
    - It is also common that the interviewer asks you extension questions, such as how you would handle the problem if the whole input is too large to fit into memory, or if the input arrives as a stream.
    - This is a common follow-up question at Google, where they care a lot about scale. The answer is usually a divide-and-conquer approach — perform distributed processing of the data and only read certain chunks of the input from disk into memory, write the output back to disk and combine them later.

<hr>

# Python 

# Introduction
***Goals:***
1. Get familiar with execution process
2. Get versed with IDE (PyCharm), Debugging

# Advanced Topics
***Goals:***
1. Lambda Functions
2. Decorators
3. Iterators and Generators
4. Exception Handling

# Data Structures
***Goals:***
1. Datatypes and in-built methods in Python  
2. Universal Data structures and implementation

# Object Oriented Programming
***Goals:***
1. OOPs concepts knowledge accuracy
2. OOP implementation

<hr>