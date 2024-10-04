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
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 63)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(430, 41)
        self._label1.TabIndex = 0
        self._label1.Text = "Amount Recieved: $"
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(380, 41)
        self._label2.TabIndex = 1
        self._label2.Text = "Purchase Price: $"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 121)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(430, 41)
        self._label3.TabIndex = 2
        self._label3.Text = "Change Due: $"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 210)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(284, 41)
        self._label4.TabIndex = 3
        self._label4.Text = "Dollars:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 260)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(284, 41)
        self._label5.TabIndex = 4
        self._label5.Text = "Quarters:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 310)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(284, 41)
        self._label6.TabIndex = 5
        self._label6.Text = "Dimes:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(302, 210)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(284, 41)
        self._label7.TabIndex = 6
        self._label7.Text = "Nickels:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(302, 260)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(284, 41)
        self._label8.TabIndex = 7
        self._label8.Text = "Pennies:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(302, 310)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(284, 41)
        self._label9.TabIndex = 8
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Black
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.White
        self._textBox1.Location = System.Drawing.Point(320, 9)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(198, 44)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Black
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.White
        self._textBox2.Location = System.Drawing.Point(356, 63)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(162, 44)
        self._textBox2.TabIndex = 10
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Black
        self._button1.Location = System.Drawing.Point(317, 310)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(255, 41)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Red
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Black
        self._button2.Location = System.Drawing.Point(116, 354)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(255, 41)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Black
        self._button3.Location = System.Drawing.Point(377, 354)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(255, 41)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.Black
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.White
        self._label10.Location = System.Drawing.Point(267, 121)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(251, 41)
        self._label10.TabIndex = 15
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self.ClientSize = System.Drawing.Size(720, 407)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label1Click(self, sender, e):
        pass



    def Button1Click(self, sender, e):
        #Calc
        price    = float(self._textBox1.Text)
        payed    = float(self._textBox2.Text)
        change   = payed - price
        dollars  = change // 1
        quarters = (change - dollars) // .25
        dimes    = (change - dollars - (quarters*.25)) // .10
        nickels  = (change - dollars - (quarters*.25) - (dimes*.1)) // .05
        pennies  = (change - dollars - (quarters*.25) - (dimes*.1) - (nickels*.05)) // .01
        
        self._label10.Text = "%.2f" % (change)
        self._label4.Text  = "" + str(int(dollars))
        self._label5.Text  = "" + str(int(quarters))
        self._label6.Text  = "" + str(int(dimes))
        self._label7.Text  = "" + str(int(nickels))
        self._label8.Text  = "" + str(int(pennies))

    def Button2Click(self, sender, e):
        self._label10.Text = ""
        self._label4.Text  = ""
        self._label5.Text  = ""
        self._label6.Text  = ""
        self._label7.Text  = ""
        self._label8.Text  = ""
        self._textBox1.Text= ""
        self._textBox2.Text= ""

    def Button3Click(self, sender, e):
        Application.Exit()