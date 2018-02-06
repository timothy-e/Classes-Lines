class Line:
    '''Fields: slope(anyof Int Float "undefined"), intercept (anyof Int Float)
          '''  
    
    def __init__(self,slope,intercept):
        self.slope = slope
        self.intercept = intercept
        
        
    def __repr__(self):
        s1 = "Y = {0:.2f}X + {1:.2f}"
        s2 = "X = {0:.2f}"
        s3 = "Y = {0:.2f}"
        if self.slope=="undefined":
            return s2.format(self.intercept)
        elif self.slope==0:
            return s3.format(self.intercept)
        else:
            return s1.format(self.slope, self.intercept)
    
    def __eq__(self, other):
            return type(other) == type(self) and self.slope == other.slope and \
                   self.intercept == other.intercept    
        
    
    def points_to_line(x1,y1,x2,y2):
        if x2 == x1:
            return Line("undefined", x1)
        else:
            return Line((y2 - y1)/(x2 - x1), y1 - ((y2 - y1)/(x2 - x1) * x1))
        
    def perpendicular_line(self,x,y):
        if self.slope == "undefined":
            return Line(0, y)
        elif self.slope == 0:
            return Line("undefined", x)
        else:
            return Line(-1 / self.slope, y + ((1 / self.slope) * x))
        

    def parallel(self, other):
        return self.slope == other.slope \
               and not self.intercept == other.intercept
    
    def intersect(self, other):
        if self.slope == other.slope:
            return False
        elif self.slope == "undefined":
            y = other.slope * self.intercept + other.intercept
            return [self.intercept, y]
        elif other.slope == "undefined":
            y = self.slope * other.intercept + self.intercept
            return [other.intercept, y]
        else:
            x = (other.intercept - self.intercept)/(self.slope - other.slope)
            y = self.slope * x + self.intercept
            return [x, y]
            
# end of Line class
L5=Line("undefined",10)
L6=Line(0,5)
