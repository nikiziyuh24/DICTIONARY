print("Welcome to the Math Dictionary!\n")

dictionary = { 
    "Abacus": "An early counting tool used for basic arithmetic.",
    "Absolute Value": "Always a positive number.",
    "Acute Angle": "An angle whose measure is between zero degrees and 90 degrees, or with less than 90-degree radians.",
    "Addend": "A number involved in an addition.",
    "Algebra": "The branch of mathematics that substitutes letters for numbers to solve for unknown values.",
    "Algorithm": "A procedure or set of steps used to solve a mathematical computation.",
    "Angle": "Two rays sharing the same endpoint.",
    "Area": "The two-dimensional space taken up by an object or shape, given in square units.",
    "Base": "The bottom of a shape or three-dimensional object.",
    "Bar Graph": "A graph that represents data visually using bars of different heights or lengths.",
    "Binomial": " A polynomial equation with two terms usually joined by a plus or minus sign.",
    "Bell Curve": "The center of a bell curve contains the highest value points.",
    "Calculus": "The study of motion in which changing values are studied.",
    "Capacity": "The volume of substance that a container will hold.",
    "Chord": "A segment joining two points on a circle.",
    "Circumference": "The complete distance around a circle or a square.",
    "Complementary Angles": "Two angles that together equal 90 degrees.",
    "Constant": "A value that does not change.",
    "Decagon": "A polygon or shape with ten angles and ten straight lines.",
    "Decimal": "A real number on the base ten standard numbering system.",
    "Denominator": "The bottom number of a fraction.",
    "Edge": "A line is where two faces meet in a three-dimensional structure.",
    "Endpoint": "The point at which a line or curve ends.",
    "Equation": "A statement that shows the equality of two expressions by joining them with an equals sign.",
    "Even Numbers": "A number that can be divided or is divisible by 2.",
    "Face": "The flat surfaces on a three-dimensional object.",
    "Factoring": "The process of breaking numbers down into all of their factors.",
    "Figure": "Two-dimensional shapes.",
    "Finite": "Not infinite; has an end.",
    "Geometry": "The study of lines, angles, shapes, and their properties.",
    "Greatest Common Factor": "The largest number common to each set of factors that divides both numbers exactly.",
}

while True:
    word = input("\nEnter a Math term: ")
   
    if word in dictionary:
         print(dictionary[word])
    else: 
         print("That term isn't in dictionary yet.")
