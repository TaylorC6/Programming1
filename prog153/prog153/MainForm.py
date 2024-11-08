import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 32)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(649, 39)
        self._label1.TabIndex = 0
        self._label1.Text = "Annual Salary:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Silver
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 266)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(195, 59)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(241, 34)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(411, 35)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(335, 119)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(317, 35)
        self._textBox2.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 117)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(649, 39)
        self._label2.TabIndex = 3
        self._label2.Text = "Pay Periods Per Year:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 205)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(649, 39)
        self._label3.TabIndex = 5
        self._label3.Text = "Salary Pay Per Period:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Aqua
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(335, 210)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(317, 30)
        self._label4.TabIndex = 6
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Silver
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(241, 266)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(195, 59)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Silver
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(467, 266)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(195, 59)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightBlue
        self.ClientSize = System.Drawing.Size(674, 370)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog153"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        annual = float(self._textBox1.Text)
        per = int(self._textBox2.Text)
        salary = annual / per
        self._label4.Text = str(round(salary, 2))

    def Button2Click(self, sender, e):
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()