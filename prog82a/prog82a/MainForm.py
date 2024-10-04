import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Aquamarine
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label1.Location = System.Drawing.Point(12, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(552, 39)
        self._label1.TabIndex = 0
        self._label1.Text = "Speed Limit:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Aquamarine
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label2.Location = System.Drawing.Point(12, 71)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(552, 39)
        self._label2.TabIndex = 1
        self._label2.Text = "Vehicle Speed:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Aquamarine
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label3.Location = System.Drawing.Point(12, 166)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(552, 39)
        self._label3.TabIndex = 2
        self._label3.Text = "Fine: $"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(29, 288)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(213, 49)
        self._button1.TabIndex = 3
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(178, 233)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(213, 49)
        self._button2.TabIndex = 4
        self._button2.Text = "Calculate"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(328, 288)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(213, 49)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(247, 29)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(302, 26)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(247, 79)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(302, 26)
        self._textBox2.TabIndex = 7
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self.ClientSize = System.Drawing.Size(576, 426)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()





    def Button2Click(self, sender, e):
        limit = int(self._textBox1.Text)
        speed = int(self._textBox2.Text)
        miles_over = speed - limit
        fine = 20.0 + (miles_over * 5)
        self._label3.Text = "Fine: $ %.2f" % fine
        

    def Button1Click(self, sender, e):
        self._label3.Text = "Fine: $"
        self._textBox2.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()