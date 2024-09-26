import math
import System.Drawing
import System.Windows.Forms

from math import *
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(111, 72)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(437, 53)
        self._label1.TabIndex = 0
        self._label1.Text = "Ax^2 + Bx + C"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(75, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(515, 53)
        self._label2.TabIndex = 1
        self._label2.Text = " A:        B:        C:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(155, 16)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 35)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(310, 16)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 35)
        self._textBox2.TabIndex = 3
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(476, 16)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 35)
        self._textBox3.TabIndex = 4
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.IndianRed
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 170)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(291, 92)
        self._label3.TabIndex = 5
        self._label3.Text = "Root 1:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.IndianRed
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(355, 170)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(291, 92)
        self._label4.TabIndex = 6
        self._label4.Text = "Root 2:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(96, 318)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(159, 51)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(261, 318)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(159, 51)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(426, 318)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(159, 51)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(658, 413)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label3Click(self, sender, e):
        pass


    def Button1Click(self, sender, e):
        	a = float(self._textBox1.Text)
        	b = float(self._textBox2.Text)
        	c = float(self._textBox3.Text)
        	quadadd = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        	quadsub = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        	self._label3.Text = "Root 1: " + str(quadadd)
        	self._label4.Text = "Root 2: " + str(quadsub)

    def Button2Click(self, sender, e):
        self._label3.Text = "Root 1:"
        self._label4.Text = "Root 2:"
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()