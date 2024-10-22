import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Chocolate
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(377, 276)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(175, 51)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Chocolate
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(196, 276)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(175, 51)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Chocolate
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(15, 276)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(175, 51)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Orange
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(9, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(546, 49)
        self._label1.TabIndex = 8
        self._label1.Text = "Enter a Number:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Chocolate
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(297, 17)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(245, 35)
        self._textBox1.TabIndex = 9
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Orange
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(10, 73)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(546, 191)
        self._label2.TabIndex = 10
        self._label2.Click += self.Label2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.ForestGreen
        self.ClientSize = System.Drawing.Size(562, 347)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog_162a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        input = int(self._textBox1.Text)
        mul = input
        for mul in range(input, 1, -1):
            
            
        self._label2.Text = "The value of " + str(input) + "! is " + str(output)

    def Button2Click(self, sender, e):
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label2Click(self, sender, e):
        pass