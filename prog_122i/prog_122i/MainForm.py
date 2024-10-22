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
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(412, 342)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(175, 51)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(231, 342)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(175, 51)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(50, 342)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(175, 51)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.MediumAquamarine
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 37
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(631, 300)
        self._listBox1.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DeepPink
        self.ClientSize = System.Drawing.Size(657, 409)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog_122i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Num\tCube Root\tCubed"
        self._listBox1.Items.Add(heading)
        for num in range(-25,26):
            cubed = 0.0
            if num < 0:
                posnum = abs(num)
                cubed = -(float(posnum ** (1.0 / 3)))
            else:
                cubed = float(num ** (1.0 / 3))
                cube = num ** 3
                line = str(num) + "\t" + str(round(cubed, 5)) + "\t\t" + str(cube)
                self._listBox1.Items.Add(line)

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()