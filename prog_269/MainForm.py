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
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSteelBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(339, 205)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(158, 50)
        self._button3.TabIndex = 41
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(176, 205)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(158, 50)
        self._button2.TabIndex = 40
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 205)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(158, 50)
        self._button1.TabIndex = 39
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Turquoise
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(368, 17)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(277, 33)
        self._textBox2.TabIndex = 38
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Turquoise
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(273, 83)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(214, 33)
        self._textBox1.TabIndex = 37
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Turquoise
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(273, 149)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(214, 33)
        self._label3.TabIndex = 36
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.SlateBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(12, 139)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(485, 51)
        self._label4.TabIndex = 35
        self._label4.Text = "% of Calories From Fat:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.SlateBlue
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(12, 75)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(485, 51)
        self._label2.TabIndex = 34
        self._label2.Text = "# of Fat Grams in Food:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.SlateBlue
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.White
        self._label10.Location = System.Drawing.Point(12, 9)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(643, 51)
        self._label10.TabIndex = 33
        self._label10.Text = "Input Runner Name, Race Time:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(678, 262)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label10)
        self.Name = "MainForm"
        self.Text = "prog_269"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        inp = str(self._textBox1.Text)
        name = []
        time = []
        for i in range(inp):
            while i != ",":
                name.append(i)