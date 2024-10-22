﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 37
        self._listBox1.Location = System.Drawing.Point(13, 9)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(549, 226)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(23, 272)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(175, 51)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(204, 272)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(175, 51)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(385, 272)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(175, 51)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(574, 341)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog_122d"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "x\t\ty"
        self._listBox1.Items.Add(heading)
        for num in range(-12,17):
            Y = (num ** 6 - 3 * num ** 5 - 93 * num ** 4 + 87 * num ** 3 + 1596 * num ** 2 - 1380 * num - 2800)
            line = str(num) + "\t\t" + str(Y)
            self._listBox1.Items.Add(line)

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def MainFormLoad(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()