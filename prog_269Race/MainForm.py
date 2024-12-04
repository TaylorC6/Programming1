import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(7, 399)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(148, 50)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(324, 399)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(158, 50)
        self._button3.TabIndex = 41
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(161, 399)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(158, 50)
        self._button2.TabIndex = 40
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkSlateGray
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(2, 131)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(485, 51)
        self._label4.TabIndex = 35
        self._label4.Text = "Name 3, Time"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkSlateGray
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(2, 67)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(485, 51)
        self._label2.TabIndex = 34
        self._label2.Text = "Name 2, Time"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DarkSlateGray
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.White
        self._label10.Location = System.Drawing.Point(2, 1)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(485, 51)
        self._label10.TabIndex = 33
        self._label10.Text = "Name 1, Time"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkSlateGray
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(2, 325)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(485, 51)
        self._label1.TabIndex = 44
        self._label1.Text = "3rd Place Runner:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label1.Click += self.Label1Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DarkSlateGray
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(2, 261)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(485, 51)
        self._label5.TabIndex = 43
        self._label5.Text = "2nd Place Runner:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.DarkSlateGray
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(2, 195)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(485, 51)
        self._label6.TabIndex = 42
        self._label6.Text = "1st Place Runner:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label6.Click += self.Label6Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(263, 202)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(214, 33)
        self._label3.TabIndex = 36
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(324, 138)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(153, 33)
        self._textBox3.TabIndex = 45
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox4.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(166, 138)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(153, 33)
        self._textBox4.TabIndex = 46
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(166, 74)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(153, 33)
        self._textBox1.TabIndex = 48
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(324, 74)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(153, 33)
        self._textBox2.TabIndex = 47
        # 
        # textBox5
        # 
        self._textBox5.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox5.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(166, 8)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(153, 33)
        self._textBox5.TabIndex = 50
        # 
        # textBox6
        # 
        self._textBox6.BackColor = System.Drawing.Color.MediumSeaGreen
        self._textBox6.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(324, 8)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(153, 33)
        self._textBox6.TabIndex = 49
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.Black
        self._label7.Location = System.Drawing.Point(217, 205)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(260, 30)
        self._label7.TabIndex = 51
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label7.Click += self.Label7Click
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.Color.Black
        self._label8.Location = System.Drawing.Point(217, 271)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(260, 30)
        self._label8.TabIndex = 52
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label8.Click += self.Label8Click
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.Color.Black
        self._label9.Location = System.Drawing.Point(217, 335)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(260, 30)
        self._label9.TabIndex = 53
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label9.Click += self.Label9Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Green
        self.ClientSize = System.Drawing.Size(489, 461)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog_269"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        name1 = str(self._textBox5.Text)
        name2 = str(self._textBox1.Text)
        name3 = str(self._textBox4.Text)
        Time1 = str(self._textBox6.Text)
        Time2 = str(self._textBox2.Text)
        Time3 = str(self._textBox3.Text)
        First = min(Time1, Time2, Time3)
        Sec = 0
        Third = max(Time1, Time2, Time3)
        if Time1 != First and Time1 != Third:
            Sec = Time1
        elif Time2 != First and Time2 != Third:
            Sec = Time2
        elif Time3 != First and Time3 != Third:
            Sec = Time3
        if Time1 == First:
            self._label7.Text = str(name1)
        elif Time2 == First:
            self._label7.Text = str(name2)
        elif Time3 == First:
            self._label7.Text = str(name3)
        if Time1 == Sec:
            self._label8.Text = str(name1)
        elif Time2 == Sec:
            self._label8.Text = str(name2)
        elif Time3 == Sec:
            self._label8.Text = str(name3)
        if Time1 == Third:
            self._label9.Text = str(name1)
        elif Time2 == Third:
            self._label9.Text = str(name2)
        elif Time3 == Third:
            self._label9.Text = str(name3)
        
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""
        self._label9.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()