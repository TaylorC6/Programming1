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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Navy
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(625, 40)
        self._label1.TabIndex = 0
        self._label1.Text = "Radius:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Navy
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(13, 80)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(624, 278)
        self._label2.TabIndex = 1
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Navy
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(13, 214)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(624, 144)
        self._label3.TabIndex = 2
        self._label3.Text = "Circumference:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(247, 214)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(377, 44)
        self._label4.TabIndex = 3
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightBlue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(118, 108)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(506, 44)
        self._label5.TabIndex = 4
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Navy
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(13, 108)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 44)
        self._label6.TabIndex = 5
        self._label6.Text = "Area:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.LightBlue
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(137, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(487, 31)
        self._textBox1.TabIndex = 6
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(33, 282)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(190, 55)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PaleGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(229, 282)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(190, 55)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PaleGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(425, 282)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(190, 55)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(13, 49)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(181, 31)
        self._label7.TabIndex = 10
        self._label7.Text = "Circles"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(649, 367)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        pi = 3.14159
        Radius = float(self._textBox1.Text)
        Circum = 2 * pi * Radius
        Area = pi * Radius ** 2
        self._label4.Text = "%.3f" % Circum
        self._label5.Text = "%.3f" % Area

    def Button2Click(self, sender, e):
        self._label4.Text = ""
        self._label5.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()