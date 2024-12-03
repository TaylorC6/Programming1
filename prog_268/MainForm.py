﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label10 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DarkSlateGray
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.White
        self._label10.Location = System.Drawing.Point(12, 13)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(485, 51)
        self._label10.TabIndex = 22
        self._label10.Text = "# of Calories in Food:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkSlateGray
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(12, 79)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(485, 51)
        self._label2.TabIndex = 24
        self._label2.Text = "# of Fat Grams in Food:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(273, 153)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(214, 33)
        self._label3.TabIndex = 27
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkSlateGray
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(12, 143)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(485, 51)
        self._label4.TabIndex = 26
        self._label4.Text = "% of Calories From Fat:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(273, 87)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(214, 33)
        self._textBox1.TabIndex = 28
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(273, 21)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(214, 33)
        self._textBox2.TabIndex = 29
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 209)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(158, 50)
        self._button1.TabIndex = 30
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(176, 209)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(158, 50)
        self._button2.TabIndex = 31
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(339, 209)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(158, 50)
        self._button3.TabIndex = 32
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Teal
        self.ClientSize = System.Drawing.Size(509, 283)
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
        self.Text = "prog_268"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label8Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        cals = int(self._textBox2.Text)
        fats = int(self._textBox1.Text)
        cd = float(fats * 9)
        percent = (cd / cals) * 100
        self._label3.Text = "%" + "%.2f" % (percent)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()