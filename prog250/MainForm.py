import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.ForeColor = System.Drawing.Color.White
        self._radioButton1.Location = System.Drawing.Point(29, 65)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(228, 37)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Standard Adult"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.ForeColor = System.Drawing.Color.White
        self._radioButton2.Location = System.Drawing.Point(28, 108)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(228, 37)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Child"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.ForeColor = System.Drawing.Color.White
        self._radioButton3.Location = System.Drawing.Point(27, 190)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(228, 37)
        self._radioButton3.TabIndex = 3
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Senior Citizen"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.ForeColor = System.Drawing.Color.White
        self._radioButton4.Location = System.Drawing.Point(28, 147)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(228, 37)
        self._radioButton4.TabIndex = 2
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Student"
        self._radioButton4.UseVisualStyleBackColor = False
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(12, 19)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(308, 235)
        self._label1.TabIndex = 4
        self._label1.Text = "Membership Type:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(326, 19)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(308, 235)
        self._label2.TabIndex = 5
        self._label2.Text = "Options:"
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.ForeColor = System.Drawing.Color.White
        self._checkBox1.Location = System.Drawing.Point(338, 89)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(194, 37)
        self._checkBox1.TabIndex = 6
        self._checkBox1.Text = "Yoga"
        self._checkBox1.UseVisualStyleBackColor = False
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.ForeColor = System.Drawing.Color.White
        self._checkBox2.Location = System.Drawing.Point(338, 133)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(194, 37)
        self._checkBox2.TabIndex = 7
        self._checkBox2.Text = "Karate"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.ForeColor = System.Drawing.Color.White
        self._checkBox3.Location = System.Drawing.Point(338, 176)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(261, 37)
        self._checkBox3.TabIndex = 8
        self._checkBox3.Text = "Personal Trainer"
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(12, 260)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(308, 235)
        self._label3.TabIndex = 9
        self._label3.Text = "Membership Length:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(326, 260)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(308, 235)
        self._label4.TabIndex = 10
        self._label4.Text = "Membership Fees:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(63, 315)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(257, 91)
        self._label5.TabIndex = 11
        self._label5.Text = "Enter # of Months:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(52, 422)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(218, 40)
        self._textBox1.TabIndex = 12
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.White
        self._label7.Location = System.Drawing.Point(414, 347)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(183, 91)
        self._label7.TabIndex = 14
        self._label7.Text = "Total:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gray
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(340, 394)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(123, 44)
        self._button1.TabIndex = 17
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gray
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(485, 394)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(123, 44)
        self._button2.TabIndex = 18
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gray
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(414, 444)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(123, 44)
        self._button3.TabIndex = 19
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(485, 300)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(142, 34)
        self._label8.TabIndex = 20
        self._label8.Click += self.Label8Click
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.White
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(485, 347)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(142, 34)
        self._label9.TabIndex = 21
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.White
        self._label10.Location = System.Drawing.Point(326, 300)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(183, 91)
        self._label10.TabIndex = 13
        self._label10.Text = "Monthly Fees:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(645, 503)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog250"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        
        base = 0.0
        months = int(self._textBox1.Text)
        fee = 0.0
        tot = 0.0
        
        if self._radioButton1.Checked:
            base = 40
        elif self._radioButton2.Checked:
            base = 20
        elif self._radioButton4.Checked:
            base = 25
        elif self._radioButton3.Checked:
            base = 30
        else:
            MessageBox.Show("Membership Type Not Selected!")
            
        if self._checkBox1.Checked:
            base += 10
        if self._checkBox2.Checked:
            base += 30
        if self._checkBox3.Checked:
            base += 50
        
        fee = base
        
        if months <= 3:
            fee = base
        elif months >= 4 and months <= 6:
            fee -= 0.05*fee
        elif months >= 7 and months <= 9:
            fee -= 0.08*fee
        elif months >= 10:
            fee -= 0.1*fee
        tot = fee*months
        
        self._label8.Text = "$ %.2f" % (fee)
        self._label9.Text = "$ %.2f" % (tot)
        
        
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label8.Text = ""
        self._label9.Text = ""

    def Label8Click(self, sender, e):
        pass

    def Label6Click(self, sender, e):
        pass