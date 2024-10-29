import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.BurlyWood
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 131)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(546, 202)
        self._label2.TabIndex = 16
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.SandyBrown
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(11, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(546, 49)
        self._label1.TabIndex = 14
        self._label1.Text = "# of Guests:"
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.SeaShell
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(380, 351)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(175, 51)
        self._button3.TabIndex = 13
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.SeaShell
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(199, 351)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(175, 51)
        self._button2.TabIndex = 12
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.SeaShell
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(18, 351)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(175, 51)
        self._button1.TabIndex = 11
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.SandyBrown
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 67)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(546, 49)
        self._label3.TabIndex = 17
        self._label3.Text = "# of Chairs:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Chocolate
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(230, 21)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(314, 35)
        self._textBox1.TabIndex = 15
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Chocolate
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(231, 75)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(314, 35)
        self._textBox2.TabIndex = 18
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self.ClientSize = System.Drawing.Size(572, 414)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog_162h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        guests = int(self._textBox1.Text)
        chairs = int(self._textBox2.Text)
        stand = guests - chairs
        perms = stand
        s = stand + 1
        for num in range(s, guests):
            perms *= num
            self._label2.Text = "Guests: " + str(guests) + "\nChairs: " + str(chairs) + "\nPermutations: " + str(perms) + "\nStanding: " + str(stand)
            

    def Button2Click(self, sender, e):
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()