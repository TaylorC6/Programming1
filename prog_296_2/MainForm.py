import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox6 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox6
        # 
        self._textBox6.BackColor = System.Drawing.Color.LawnGreen
        self._textBox6.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(189, 16)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(295, 33)
        self._textBox6.TabIndex = 67
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.LawnGreen
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(189, 82)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(295, 33)
        self._textBox2.TabIndex = 65
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.LawnGreen
        self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(189, 146)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(295, 33)
        self._textBox3.TabIndex = 63
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.DimGray
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(9, 203)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(485, 187)
        self._label6.TabIndex = 60
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LawnGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(331, 407)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(158, 50)
        self._button3.TabIndex = 59
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LawnGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(168, 407)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(158, 50)
        self._button2.TabIndex = 58
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DimGray
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(9, 139)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(485, 51)
        self._label4.TabIndex = 57
        self._label4.Text = "Package C:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DimGray
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(9, 75)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(485, 51)
        self._label2.TabIndex = 56
        self._label2.Text = "Package B:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DimGray
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.White
        self._label10.Location = System.Drawing.Point(9, 9)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(485, 51)
        self._label10.TabIndex = 55
        self._label10.Text = "Package A:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LawnGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(14, 407)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(148, 50)
        self._button1.TabIndex = 54
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDark
        self.ClientSize = System.Drawing.Size(500, 465)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog_296_2"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        A = int(self._textBox6.Text)
        B = int(self._textBox2.Text)
        C = int(self._textBox3.Text)
        discount = 0.0
        if A >= 10 and A <= 19:
            discount = 20.0
        self._label6.Text = str(discount)

    def Button2Click(self, sender, e):
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox6.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()