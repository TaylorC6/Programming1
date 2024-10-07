import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Maroon
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(304, 171)
        self._label1.TabIndex = 0
        self._label1.Text = "Inputs:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(56, 66)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(247, 31)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(56, 122)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(247, 31)
        self._textBox2.TabIndex = 2
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Location = System.Drawing.Point(13, 198)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(634, 225)
        self._label2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(28, 215)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(310, 42)
        self._label3.TabIndex = 4
        self._label3.Text = "Sum:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(28, 266)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(310, 42)
        self._label4.TabIndex = 5
        self._label4.Text = "Difference:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(28, 317)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(310, 42)
        self._label5.TabIndex = 6
        self._label5.Text = "Product:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(192, 368)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(302, 42)
        self._label7.TabIndex = 8
        self._label7.Text = "Average:"
        self._label7.Click += self.Label7Click
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(334, 216)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(302, 42)
        self._label8.TabIndex = 9
        self._label8.Text = "Distance:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(334, 264)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(302, 42)
        self._label9.TabIndex = 10
        self._label9.Text = "Min:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(334, 317)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(302, 42)
        self._label10.TabIndex = 11
        self._label10.Text = "Max:"
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.Maroon
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.Color.White
        self._label11.Location = System.Drawing.Point(13, 63)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(37, 45)
        self._label11.TabIndex = 12
        self._label11.Text = "1."
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.Maroon
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.Color.White
        self._label12.Location = System.Drawing.Point(12, 119)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(37, 45)
        self._label12.TabIndex = 13
        self._label12.Text = "2."
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(324, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(323, 53)
        self._button1.TabIndex = 14
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(323, 72)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(323, 53)
        self._button2.TabIndex = 15
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(324, 131)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(323, 53)
        self._button3.TabIndex = 16
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self.ClientSize = System.Drawing.Size(659, 432)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog88a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Sum  = num1 + num2
        Dif  = num1 - num2
        Prod = num1 * num2
        Avg  = (num1 + num2) / 2
        Dist = abs(Dif)
        Max  = 0
        Min  = 0
        if num1 >= num2:
            Max = num1
        else:
            Max = num2
            
        if Max == num1: # If max has same value as num1 (==)
            Min = num2
        else:
            Min = num1
            
        self._label3.Text  = "Sum: "        + str(Sum)
        self._label4.Text  = "Difference: " + str(Dif)
        self._label5.Text  = "Product: "    + str(Prod)
        self._label7.Text  = "Average: "    + str(Avg)
        self._label10.Text = "Max: "        + str(Max)
        self._label9.Text  = "Min: "        + str(Min)
        self._label8.Text  = "Distance: "   + str(Dist)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label3.Text   = "Sum:"
        self._label4.Text   = "Difference:"
        self._label5.Text   = "Product:"
        self._label7.Text   = "Average:"
        self._label8.Text   = "Max:"
        self._label9.Text   = "Min:"
        self._label10.Text  = "Abs Value:"

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label7Click(self, sender, e):
        pass