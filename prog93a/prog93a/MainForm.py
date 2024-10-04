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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(427, 45)
        self._label1.TabIndex = 0
        self._label1.Text = "Killowatts Used:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(251, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(179, 40)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 54)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(427, 55)
        self._label2.TabIndex = 2
        self._label2.Text = "-----------------------------------------"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 102)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(427, 209)
        self._label3.TabIndex = 3
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 92)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(427, 36)
        self._label4.TabIndex = 4
        self._label4.Text = "Base Rate:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 123)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(427, 31)
        self._label5.TabIndex = 5
        self._label5.Text = "Surcharge:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 185)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(427, 36)
        self._label6.TabIndex = 7
        self._label6.Text = "Pay This Amount:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(12, 154)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(427, 36)
        self._label7.TabIndex = 6
        self._label7.Text = "Citytax:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(12, 216)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(427, 36)
        self._label8.TabIndex = 8
        self._label8.Text = "After May 20th Pay:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(294, 92)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(136, 36)
        self._label9.TabIndex = 9
        self._label9.Text = "$"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label9.Click += self.Label9Click
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(294, 123)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(136, 36)
        self._label10.TabIndex = 10
        self._label10.Text = "$"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(294, 186)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(136, 36)
        self._label11.TabIndex = 12
        self._label11.Text = "$"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(294, 155)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(136, 36)
        self._label12.TabIndex = 11
        self._label12.Text = "$"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(294, 216)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(136, 36)
        self._label13.TabIndex = 13
        self._label13.Text = "$"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(16, 265)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(136, 36)
        self._button1.TabIndex = 14
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(158, 265)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(136, 36)
        self._button2.TabIndex = 15
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(300, 265)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(136, 36)
        self._button3.TabIndex = 16
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self.ClientSize = System.Drawing.Size(451, 320)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label9Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        killowatts = int(self._textBox1.Text)
        base = int(killowatts * 0.0475)
        sur = float(base * 0.1)
        tax = float(base * 0.03)
        total = float(base + sur + tax)
        late = float(total * 1.04)
        self._label9.Text = "$ %.2f" % base
        self._label10.Text = "$ %.2f" % sur
        self._label12.Text = "$ %.2f" % tax
        self._label11.Text = "$ %.2f" % total
        self._label13.Text = "$ %.2f" % late

    def Button2Click(self, sender, e):
        self._label9.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()