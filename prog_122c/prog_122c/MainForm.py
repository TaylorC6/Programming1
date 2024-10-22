import System.Drawing
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
        self._listBox1.BackColor = System.Drawing.Color.DarkSalmon
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.ForeColor = System.Drawing.Color.Maroon
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 37
        self._listBox1.Location = System.Drawing.Point(2, 2)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(558, 226)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Salmon
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(5, 249)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(181, 63)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Salmon
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(192, 249)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(181, 63)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Salmon
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(379, 249)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(181, 63)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Firebrick
        self.ClientSize = System.Drawing.Size(564, 336)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog_122c"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = ("#\t+1\t*2\t^2")
        self._listBox1.Items.Add(heading)
        for num in range(2,21, 2):
            plus = int(num + 1) # +1
            dub = int(num * 2) # double
            square = int(num ** 2) # squared
            line = str(num) + "\t" + str(plus) + "\t" + str(dub) + "\t" + str(square)
            self._listBox1.Items.Add(line) 

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()