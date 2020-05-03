from big_ol_pile_of_manim_imports import *

class MoveVector(Scene):
    def construct(self):
        vector = Vector(direction=RIGHT)
        end_point = (4,0,0)
        animation = ApplyMethod(vector.shift,end_point)
        self.play(animation)
        
class Grid2(Scene):
    
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    
    grid = []
    
    def construct(self):
        n = int(input())
        screen_grid=ScreenGrid()
        self.add(screen_grid)

        grid_box = [[]*n]*n
        
        for i in range(0, n): 
            self.grid.append(input().strip())

        for i in range(n):
            for j in range(n):
                #square = Square(width=4,fill_color=GOLD_B, fill_opacity=0, color=GOLD_A)   
                
                if self.grid[i][j] == 'b':
                    
                    grid_box[i][j] = Rectangle(fill_color=GOLD_B,height=1, fill_opacity=1,width=1)
                    
                elif self.grid[i][j] == 'p':
                    grid_box[i][j] = Rectangle(fill_color=GREEN_A,height=1, width=1)
                    
                else:
                    grid_box[i][j] = Rectangle(height=1, width=1)

                grid_box[i][j].move_to(np.array([i-3,j-3,0]))
                
                self.play(ShowCreation(grid_box[i][j]))
                
        #gd.row_of_rows(m, m, 50)
        #displayPathtoPrincess(m,grid)
        
        
        
    
                
    def pathfinding(dirmat,x,y,n):
        gd.bob.goto(50*(y)+25,50*(n-x-1)+25)
        drawBox(x,y,10,"red",n)
        if x == 0 and y == 0:
            return
        d = dirmat[x][y]
    
        pathfinding(dirmat,x - dr[d],y - dc[d] ,n)
        gd.bob.goto(50*(y)+25,50*(n-x-1)+25)
        if d == 0:
            print("up")
        elif d == 1:
            print("right")
        elif d == 2:
            print("down")
        elif d == 3:
            print("left")
    
    def displayPathtoPrincess(n,grid):
    
        r = len(grid)
        c = len(grid[0])
    
        des_u = des_v = 0
        start = (0,0)
        q = [start]
    
        visited = [[False for j in range(c)] for i in range(r)]
        visited[0][0] = True
        found = False
    
        drawBox(0,0,10,"red",n)           
    
        dirmat = [[-1 for j in range(c)] for i in range(r)]
        while q and not found:
            (u,v) = q.pop(0)
            print((u,v))

            drawBox(u,v,5,"green",n)
       
            for d in range(4):
                x = u + dr[d]
                y = v + dc[d]
            
                if x >= 0 and x < r and y >= 0 and y < c and not visited[x][y]:
                    dirmat[x][y] = d
                    q.append((x,y))
                    visited[x][y] = True
                    if grid[x][y] == 'p':
                        des_u = x
                        des_v = y

                        drawBox(x,y,10,"orange",n) 
                        found = True
                    
        pathfinding(dirmat,des_u,des_v,n)
        
        




    
                
                
        
            
class Grid(VMobject):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows":8,
        "columns":14,
        "height": FRAME_Y_RADIUS*2,
        "width": 14,
        "grid_stroke":0.5,
        "grid_color":WHITE,
        "axis_color":RED,
        "axis_stroke":2,
        "show_points":False,
        "point_radius":0,
        "labels_scale":0.5,
        "labels_buff":0,
        "number_decimals":2
    }

    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        rows=self.rows
        columns=self.columns
        grilla=Grid(width=self.width,height=self.height,rows=rows,columns=columns).set_stroke(self.grid_color,self.grid_stroke)

        vector_ii=ORIGIN+np.array((-self.width/2,-self.height/2,0))
        vector_id=ORIGIN+np.array((self.width/2,-self.height/2,0))
        vector_si=ORIGIN+np.array((-self.width/2,self.height/2,0))
        vector_sd=ORIGIN+np.array((self.width/2,self.height/2,0))

        ejes_x=Line(LEFT*self.width/2,RIGHT*self.width/2)
        ejes_y=Line(DOWN*self.height/2,UP*self.height/2)

        ejes=VGroup(ejes_x,ejes_y).set_stroke(self.axis_color,self.axis_stroke)

        divisiones_x=self.width/columns
        divisiones_y=self.height/rows

        direcciones_buff_x=[UP,DOWN]
        direcciones_buff_y=[RIGHT,LEFT]
        dd_buff=[direcciones_buff_x,direcciones_buff_y]
        vectores_inicio_x=[vector_ii,vector_si]
        vectores_inicio_y=[vector_si,vector_sd]
        vectores_inicio=[vectores_inicio_x,vectores_inicio_y]
        tam_buff=[0,0]
        divisiones=[divisiones_x,divisiones_y]
        orientaciones=[RIGHT,DOWN]
        puntos=VGroup()
        leyendas=VGroup()


        for tipo,division,orientacion,coordenada,vi_c,d_buff in zip([columns,rows],divisiones,orientaciones,[0,1],vectores_inicio,dd_buff):
            for i in range(1,tipo):
                for v_i,direcciones_buff in zip(vi_c,d_buff):
                    ubicacion=v_i+orientacion*division*i
                    punto=Dot(ubicacion,radius=self.point_radius)
                    coord=round(punto.get_center()[coordenada],self.number_decimals)
                    leyenda=TextMobject("%s"%coord).scale(self.labels_scale)
                    leyenda.next_to(punto,direcciones_buff,buff=self.labels_buff)
                    puntos.add(punto)
                    leyendas.add(leyenda)

        self.add(grilla,ejes,leyendas)
        if self.show_points==True:
            self.add(puntos)
            
class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))
        
class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.add(line)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        
class WriteText(Scene): 
    def construct(self): 
        text = TextMobject("This is a regular text")
        self.play(Write(text))
        self.wait(3)

class AddText(Scene): 
    def construct(self): 
        text = TextMobject("This is a regular text")
        self.add(text)
        self.wait(3)

class Formula(Scene): 
    def construct(self): 
        formula = TexMobject("This is a formula")
        self.play(Write(formula))
        self.wait(3)

class TypesOfText(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
            This is a regular text,
            $this is a formula$,
            $$this is a formula$$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class TypesOfText2(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
            This is a regular text,
            $\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class DisplayFormula(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
            This is a regular text,
            $\\displaystyle\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class TextInCenter(Scene):
    def construct(self):
        text = TextMobject("Text")
        self.play(Write(text))
        self.wait(3)

class TextOnTopEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(3)

class TextOnBottomEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(3)

class TextOnRightEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(RIGHT)
        self.play(Write(text))
        self.wait(3)

class TextOnLeftEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(LEFT)
        self.play(Write(text))
        self.wait(3)

class TextInUpperRightCorner(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(UP+RIGHT)
        self.play(Write(text))
        self.wait(3)

class TextInLowerLeftCorner(Scene): 
    def construct(self): 
        text = TextMobject("Text") 
        text.to_edge(LEFT+DOWN)
        self.play(Write(text))
        self.wait(3)

class CustomPosition1(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Central text")
        textM.move_to(0.25*UP) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class CustomPosition2(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Central text")
        textM.move_to(1*UP+1*RIGHT)
        self.play(Write(textM),Write(textC))
        self.wait(1)
        textM.move_to(1*UP+1*RIGHT) 
        self.play(Write(textM))
        self.wait(3)

class RelativePosition1(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.next_to(textC,LEFT,buff=1) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class RelativePosition2(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP*0.1)
        self.play(Write(textM),Write(textC))
        self.wait(3)

class RotateObject(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4) 
        self.play(Write(textM),Write(textC))
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI)
        self.wait(2)

class FlipObject(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)

class SizeTextOnLaTeX(Scene):
    def construct(self):
        textHuge = TextMobject("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
        textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
        textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = TextMobject("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = TextMobject("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)

class TextFonts(Scene):
    def construct(self):
        textNormal = TextMobject("{Roman serif text 012.\\#!?} Text")
        textItalic = TextMobject("\\textit{Italic text 012.\\#!?} Text")
        textTypewriter = TextMobject("\\texttt{Typewritter text 012.\\#!?} Text")
        textBold = TextMobject("\\textbf{Bold text 012.\\#!?} Text")
        textSL = TextMobject("\\textsl{Slanted text 012.\\#!?} Text")
        textSC = TextMobject("\\textsc{Small caps text 012.\\#!?} Text")
        textNormal.to_edge(UP)
        textItalic.next_to(textNormal,DOWN,buff=.5)
        textTypewriter.next_to(textItalic,DOWN,buff=.5)
        textBold.next_to(textTypewriter,DOWN,buff=.5)
        textSL.next_to(textBold,DOWN,buff=.5)
        textSC.next_to(textSL,DOWN,buff=.5)
        self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
        self.wait(3)
