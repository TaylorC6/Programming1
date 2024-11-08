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
        self._label8 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumSpringGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(347, 212)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(150, 35)
        self._button3.TabIndex = 24
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumSpringGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(191, 212)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(150, 35)
        self._button2.TabIndex = 23
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumSpringGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(35, 212)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(150, 35)
        self._button1.TabIndex = 22
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.MediumAquamarine
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(218, 157)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(294, 33)
        self._label8.TabIndex = 21
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(171, 94)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(342, 31)
        self._textBox3.TabIndex = 20
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(171, 50)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(342, 31)
        self._textBox2.TabIndex = 19
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(171, 9)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(342, 31)
        self._textBox1.TabIndex = 18
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.LightSeaGreen
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(1, 154)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(520, 39)
        self._label7.TabIndex = 17
        self._label7.Text = "Average Score:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumAquamarine
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(2, 90)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(520, 39)
        self._label3.TabIndex = 16
        self._label3.Text = "Score 3:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MediumAquamarine
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(2, 46)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(520, 39)
        self._label2.TabIndex = 15
        self._label2.Text = "Score 2:"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MediumAquamarine
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(2, 3)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(520, 39)
        self._label1.TabIndex = 14
        self._label1.Text = "Score 1:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkSlateGray
        self.ClientSize = System.Drawing.Size(525, 268)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog198"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        A = float(self._textBox1.Text)
        B = float(self._textBox2.Text)
        C = float(self._textBox3.Text)
        avg = (A + B + C) / 3
        self._label8.Text = "%.2f" % (avg)
        if avg > 95:
            self._label8.Text = "Congratulations! %.2f" % (avg)

    def Button2Click(self, sender, e):
        self._label8.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()