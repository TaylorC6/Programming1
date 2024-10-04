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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Brown
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(371, 36)
        self._label1.TabIndex = 0
        self._label1.Text = "Pounds:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Brown
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 62)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(372, 36)
        self._label2.TabIndex = 1
        self._label2.Text = "Shillings:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Brown
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(13, 111)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(371, 36)
        self._label3.TabIndex = 2
        self._label3.Text = "Pence:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Brown
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 161)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(593, 166)
        self._label4.TabIndex = 3
        self._label4.Text = "Decimal Pounds:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(162, 15)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(219, 31)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(162, 65)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(219, 31)
        self._textBox2.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(162, 114)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(219, 31)
        self._textBox3.TabIndex = 6
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 352)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(186, 51)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(214, 352)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(186, 51)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(419, 352)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(186, 51)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(617, 425)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog65h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label4.Text = "Decimal Pounds:"

    def Button1Click(self, sender, e):
        pounds = float(self._textBox1.Text)
        shills = float(self._textBox2.Text)
        pence  = float(self._textBox3.Text)
        
        shill = shills * 0.05
        pen   = pence  * 0.05 * 0.08333
        
        decLbs = pounds + shill + pen
        
        self._label4.Text = "Decimal Pounds: %.2f" % (decLbs)