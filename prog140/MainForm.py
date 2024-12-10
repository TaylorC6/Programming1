import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.num1 = 0.0
        self.num2 = 0.0
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._button10 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkCyan
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 8)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(303, 38)
        self._label1.TabIndex = 0
        self._label1.Text = "Number 1:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(151, 10)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(153, 35)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(150, 100)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(153, 35)
        self._textBox2.TabIndex = 3
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkCyan
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 98)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(303, 38)
        self._label2.TabIndex = 2
        self._label2.Text = "Number 2:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkCyan
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 53)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(303, 38)
        self._label3.TabIndex = 4
        self._label3.Text = "Operation:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(340, 8)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(64, 62)
        self._button1.TabIndex = 5
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(410, 8)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(64, 62)
        self._button2.TabIndex = 6
        self._button2.Text = "-"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(480, 7)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(64, 62)
        self._button3.TabIndex = 7
        self._button3.Text = "*"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.LightSeaGreen
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(480, 76)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(64, 62)
        self._button6.TabIndex = 10
        self._button6.Text = "//"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.LightSeaGreen
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(340, 76)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(64, 62)
        self._button4.TabIndex = 8
        self._button4.Text = "^"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.LightSeaGreen
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(410, 75)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(64, 62)
        self._button5.TabIndex = 9
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.Color.LightSeaGreen
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(410, 143)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(64, 62)
        self._button8.TabIndex = 12
        self._button8.Text = "%"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.LightSeaGreen
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(150, 211)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(147, 45)
        self._button9.TabIndex = 13
        self._button9.Text = "Clear"
        self._button9.UseVisualStyleBackColor = False
        # 
        # button10
        # 
        self._button10.BackColor = System.Drawing.Color.LightSeaGreen
        self._button10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button10.Location = System.Drawing.Point(315, 211)
        self._button10.Name = "button10"
        self._button10.Size = System.Drawing.Size(147, 45)
        self._button10.TabIndex = 14
        self._button10.Text = "Exit"
        self._button10.UseVisualStyleBackColor = False
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkCyan
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 143)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(303, 38)
        self._label4.TabIndex = 15
        self._label4.Text = "Result:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkTurquoise
        self.ClientSize = System.Drawing.Size(551, 263)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button10)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog140"
        self.ResumeLayout(False)
        self.PerformLayout()

    def GrabNums(self):
        self.num1 = float(self._textBox1.Text)
        self.num2 = float(self._textBox2.Text)
        
    def Button1Click(self, sender, e):
        self.GrabNums()
        self._label4.Text = "Result:       " + str(self.num1 + self.num2)
        self._label3.Text = "Operation: +"

    def Button2Click(self, sender, e):
        self.GrabNums()
        self._label4.Text = "Result:       " + str(self.num1 - self.num2)
        self._label3.Text = "Operation: -"

    def Button3Click(self, sender, e):
        self.GrabNums()
        self._label4.Text = "Result:       " + str(self.num1 * self.num2)
        self._label3.Text = "Operation: *"

    def Button4Click(self, sender, e):
        self.GrabNums()
        self._label4.Text = "Result:       " + str(self.num1 ** self.num2)
        self._label3.Text = "Operation: ^"

    def Button5Click(self, sender, e):
        self.GrabNums()
        self._label4.Text = "Result:       " + str(self.num1 / self.num2)
        self._label3.Text = "Operation: /"

    def Button6Click(self, sender, e):
        self.GrabNums()
        self._label4.Text = "Result:       " + str(self.num1 // self.num2)
        self._label3.Text = "Operation: //"

    def Button8Click(self, sender, e):
        self.GrabNums()
        self._label4.Text = "Result:       " + str(self.num1 % self.num2)
        self._label3.Text = "Operation: %"