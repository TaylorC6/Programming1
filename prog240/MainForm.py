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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 25)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(401, 38)
        self._label1.TabIndex = 0
        self._label1.Text = "Sales in Month:   $"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 78)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(401, 38)
        self._label2.TabIndex = 1
        self._label2.Text = "Advanced Pay:    $"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 132)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(401, 38)
        self._label3.TabIndex = 2
        self._label3.Text = "Commission Rate:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 184)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(401, 38)
        self._label4.TabIndex = 3
        self._label4.Text = "Commission:       $"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 237)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(401, 38)
        self._label5.TabIndex = 4
        self._label5.Text = "Net Pay:               $"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.ForestGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 295)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(127, 46)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.ForestGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(286, 295)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(127, 46)
        self._button2.TabIndex = 7
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.ForestGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(148, 295)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(127, 46)
        self._button3.TabIndex = 8
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(216, 30)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(187, 29)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(216, 83)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(187, 29)
        self._textBox2.TabIndex = 10
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.YellowGreen
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(216, 137)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(187, 26)
        self._label6.TabIndex = 11
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.YellowGreen
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(216, 189)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(187, 26)
        self._label7.TabIndex = 12
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.YellowGreen
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(216, 242)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(187, 26)
        self._label8.TabIndex = 13
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightGreen
        self.ClientSize = System.Drawing.Size(425, 353)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog240"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        sales = float(self._textBox1.Text)
        advanced = float(self._textBox2.Text)
        comR = 0.0
        if sales < 10000:
            comR = 0.05
        elif sales > 10000 and sales < 15000:
            comR = 0.1
        elif sales >= 15000 and sales < 18000:
            comR = 0.12
        elif sales >= 18000 and sales < 22000:
            comR = 0.14
        elif sales >= 22000:
            comR = 0.16
        else:
            MessageBox.Show("Error")
            
        self._label6.Text = str(sales)
        com = sales * comR
        self._label7.Text = str(com)
        net = com - advanced
        self._label8.Text = str(net)
        

    def Button3Click(self, sender, e):
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button2Click(self, sender, e):
        Application.Exit()