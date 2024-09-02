# Report

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended you open up IDLE or the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)

1. Thinking about functions, a common design is to have functions that do one thing and do it well.  This is called the Single Responsibility Principle.  What are some advantages of this design?  
2. Looking at the Single Responsibility Principle, why would it be bad design to have a function both print and return a value?
3. In practice, prints are often isolated to a certain set of functions, and every other function returns values - including strings to print. While we did not follow this rule strictly for this assignment, what are some advantages of this design?
4. A **pure** function is defined as
   * the function return values are identical for identical arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams), and
   * the function has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or input/output streams).
   * Given that definition, which functions in color_tester.py and color_blindness_driver.py are pure functions?
     * delta
     * add more functions using the * before each line and the same indentation
5. color_tester.py has a variable at the top MIN_DIFFERENCE. Why would it be helpful to declare a variable like this?
6. What `scope` does MIN_DIFFERENCE have?
7. Take a look at the following code:
    ```python
    def get_name(which):
        if which == 1:
            which = 13
            return "Who"
        else:
            which = 3
            return "Strange"

    def welcome():
        print("Welcome Doctor?")
        which = 0
        name = get_name(1)
        print(which)
        print(f"Doctor {name}")
    
    welcome() ## execute the above
    ```
    Here is a link if you want to visualize it: [Visualize](https://pythontutor.com/render.html#code=def%20get_name%28which%29%3A%0A%20%20%20%20if%20which%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20which%20%3D%2013%0A%20%20%20%20%20%20%20%20return%20%22Who%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20which%20%3D%203%0A%20%20%20%20%20%20%20%20return%20%22Strange%22%0A%0Adef%20welcome%28%29%3A%0A%20%20%20%20print%28%22Welcome%20Doctor%3F%22%29%0A%20%20%20%20which%20%3D%200%0A%20%20%20%20name%20%3D%20get_name%281%29%0A%20%20%20%20print%28which%29%0A%20%20%20%20print%28f%22Doctor%20%7Bname%7D%22%29%0A%0Awelcome%28%29%20%23%23%20execute%20the%20above&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

    * What is printed on `print(which)`? What about `print(f"Doctor {name}")` (really, use the visualizer)? 
    * Why is this the case?

## Deeper Thinking

Inclusive design often goes beyond accessible design, and is a major area of research in computer science. Take time to read up on resources, and write a paragraph (minimum) on what you learned. Make sure to include links to any resources you used. In the paragraph, I encourage you to reflect on your own experiences with inclusive design (or lack of inclusive design), and how you can use this knowledge in your own work. Also, why does this matter at all? 
