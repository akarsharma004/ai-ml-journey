import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),logging.StreamHandler()
    ]
)
# Creating logger for a module=ArithmeticApp
logger = logging.getLogger("ArithmeticApp")

#Addition
def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b}= {result}")
    return result
# Subtraction
def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a}-{b}= {result}")
    return result
# Multiplication
def multiply(a,b):
    result = a*b
    logger.debug(f"Multiply {a} * {b}= {result}")
    return result
# Division
def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Divide {a} / {b}= {result}")
        return result
    except: 
        logger.error("Division by zero error")
        return None
    
add(23,4)
subtract(10,5)
multiply(2,3)
divide(10,2)