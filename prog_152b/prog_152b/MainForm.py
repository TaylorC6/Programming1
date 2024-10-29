import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.InactiveCaptionText
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.ForeColor = System.Drawing.Color.White
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 33
        self._listBox1.Location = System.Drawing.Point(13, 13)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(384, 367)
        self._listBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(403, 180)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(186, 62)
        self._label1.TabIndex = 1
        self._label1.Text = "Calculate"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(403, 263)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(186, 62)
        self._label2.TabIndex = 2
        self._label2.Text = "Clear"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label2.Click += self.Label2Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(403, 339)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(186, 62)
        self._label3.TabIndex = 3
        self._label3.Text = "Exit"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(403, 65)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(186, 44)
        self._textBox1.TabIndex = 4
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(404, 13)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(185, 39)
        self._label4.TabIndex = 5
        self._label4.Text = "Test Value:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(607, 429)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog_152b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label3Click(self, sender, e):
        Application.Exit()

    def Label2Click(self, sender, e):
        listBox1.Items.Clear()

    def Label1Click(self, sender, e):
        test = int(self._textBox1.Text)
        for num in range(2, test + 1, 2):
            var = num
            while var <= test:
                var += var
                write = str(num) + "\t\t" + str(var)
                self._listBox1.Items.Add(write)               