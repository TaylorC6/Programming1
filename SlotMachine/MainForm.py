﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.num1 = 0 
        self.num2 = 0
        self.num3 = 0
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        resources = System.Resources.ResourceManager("SlotMachine.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._pictureBox2 = System.Windows.Forms.PictureBox()
        self._pictureBox3 = System.Windows.Forms.PictureBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._progressBar1 = System.Windows.Forms.ProgressBar()
        self._pictureBox5 = System.Windows.Forms.PictureBox()
        self._pictureBox6 = System.Windows.Forms.PictureBox()
        self._pictureBox7 = System.Windows.Forms.PictureBox()
        self._pictureBox8 = System.Windows.Forms.PictureBox()
        self._pictureBox9 = System.Windows.Forms.PictureBox()
        self._pictureBox10 = System.Windows.Forms.PictureBox()
        self._pictureBox11 = System.Windows.Forms.PictureBox()
        self._pictureBox4 = System.Windows.Forms.PictureBox()
        self._timer1 = System.Windows.Forms.Timer(self._components)
        self._pictureBox12 = System.Windows.Forms.PictureBox()
        self._pictureBox1.BeginInit()
        self._pictureBox2.BeginInit()
        self._pictureBox3.BeginInit()
        self._pictureBox5.BeginInit()
        self._pictureBox6.BeginInit()
        self._pictureBox7.BeginInit()
        self._pictureBox8.BeginInit()
        self._pictureBox9.BeginInit()
        self._pictureBox10.BeginInit()
        self._pictureBox11.BeginInit()
        self._pictureBox4.BeginInit()
        self._pictureBox12.BeginInit()
        self.SuspendLayout()
        # 
        # pictureBox1
        # 
        self._pictureBox1.BackColor = System.Drawing.Color.White
        self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox1.Location = System.Drawing.Point(13, 13)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(212, 279)
        self._pictureBox1.TabIndex = 0
        self._pictureBox1.TabStop = False
        # 
        # pictureBox2
        # 
        self._pictureBox2.BackColor = System.Drawing.Color.White
        self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox2.Location = System.Drawing.Point(248, 13)
        self._pictureBox2.Name = "pictureBox2"
        self._pictureBox2.Size = System.Drawing.Size(212, 279)
        self._pictureBox2.TabIndex = 1
        self._pictureBox2.TabStop = False
        # 
        # pictureBox3
        # 
        self._pictureBox3.BackColor = System.Drawing.Color.White
        self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox3.Location = System.Drawing.Point(482, 12)
        self._pictureBox3.Name = "pictureBox3"
        self._pictureBox3.Size = System.Drawing.Size(212, 279)
        self._pictureBox3.TabIndex = 2
        self._pictureBox3.TabStop = False
        # 
        # button1
        # 
        self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Location = System.Drawing.Point(709, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(249, 326)
        self._button1.TabIndex = 3
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(709, 355)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(249, 54)
        self._button2.TabIndex = 4
        self._button2.Text = "Pickpocket"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(709, 427)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(249, 38)
        self._label1.TabIndex = 5
        self._label1.Text = "Bet:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(780, 429)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(165, 35)
        self._textBox1.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.WhiteSmoke
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(806, 481)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(139, 34)
        self._label2.TabIndex = 8
        self._label2.Text = "100"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label2.Click += self.Label2Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Transparent
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(709, 477)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(249, 38)
        self._label3.TabIndex = 9
        self._label3.Text = "Cash:"
        # 
        # progressBar1
        # 
        self._progressBar1.Location = System.Drawing.Point(709, 536)
        self._progressBar1.Maximum = 15000
        self._progressBar1.Name = "progressBar1"
        self._progressBar1.Size = System.Drawing.Size(249, 43)
        self._progressBar1.TabIndex = 11
        # 
        # pictureBox5
        # 
        self._pictureBox5.BackColor = System.Drawing.Color.DimGray
        self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
        self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox5.Location = System.Drawing.Point(22, 322)
        self._pictureBox5.Name = "pictureBox5"
        self._pictureBox5.Size = System.Drawing.Size(69, 63)
        self._pictureBox5.TabIndex = 13
        self._pictureBox5.TabStop = False
        self._pictureBox5.Visible = False
        # 
        # pictureBox6
        # 
        self._pictureBox6.BackColor = System.Drawing.Color.DimGray
        self._pictureBox6.BackgroundImage = resources.GetObject("pictureBox6.BackgroundImage")
        self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox6.Location = System.Drawing.Point(117, 322)
        self._pictureBox6.Name = "pictureBox6"
        self._pictureBox6.Size = System.Drawing.Size(69, 63)
        self._pictureBox6.TabIndex = 14
        self._pictureBox6.TabStop = False
        self._pictureBox6.Visible = False
        # 
        # pictureBox7
        # 
        self._pictureBox7.BackColor = System.Drawing.Color.DimGray
        self._pictureBox7.BackgroundImage = resources.GetObject("pictureBox7.BackgroundImage")
        self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox7.Location = System.Drawing.Point(310, 322)
        self._pictureBox7.Name = "pictureBox7"
        self._pictureBox7.Size = System.Drawing.Size(69, 63)
        self._pictureBox7.TabIndex = 16
        self._pictureBox7.TabStop = False
        self._pictureBox7.Visible = False
        # 
        # pictureBox8
        # 
        self._pictureBox8.BackColor = System.Drawing.Color.DimGray
        self._pictureBox8.BackgroundImage = resources.GetObject("pictureBox8.BackgroundImage")
        self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox8.Location = System.Drawing.Point(215, 322)
        self._pictureBox8.Name = "pictureBox8"
        self._pictureBox8.Size = System.Drawing.Size(69, 63)
        self._pictureBox8.TabIndex = 15
        self._pictureBox8.TabStop = False
        self._pictureBox8.Visible = False
        # 
        # pictureBox9
        # 
        self._pictureBox9.BackColor = System.Drawing.Color.DimGray
        self._pictureBox9.BackgroundImage = resources.GetObject("pictureBox9.BackgroundImage")
        self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox9.Location = System.Drawing.Point(410, 322)
        self._pictureBox9.Name = "pictureBox9"
        self._pictureBox9.Size = System.Drawing.Size(69, 63)
        self._pictureBox9.TabIndex = 17
        self._pictureBox9.TabStop = False
        self._pictureBox9.Visible = False
        # 
        # pictureBox10
        # 
        self._pictureBox10.BackColor = System.Drawing.Color.DimGray
        self._pictureBox10.BackgroundImage = resources.GetObject("pictureBox10.BackgroundImage")
        self._pictureBox10.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox10.Location = System.Drawing.Point(22, 468)
        self._pictureBox10.Name = "pictureBox10"
        self._pictureBox10.Size = System.Drawing.Size(69, 99)
        self._pictureBox10.TabIndex = 18
        self._pictureBox10.TabStop = False
        self._pictureBox10.Visible = False
        # 
        # pictureBox11
        # 
        self._pictureBox11.BackColor = System.Drawing.Color.DimGray
        self._pictureBox11.BackgroundImage = resources.GetObject("pictureBox11.BackgroundImage")
        self._pictureBox11.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox11.Location = System.Drawing.Point(97, 468)
        self._pictureBox11.Name = "pictureBox11"
        self._pictureBox11.Size = System.Drawing.Size(69, 99)
        self._pictureBox11.TabIndex = 19
        self._pictureBox11.TabStop = False
        self._pictureBox11.Visible = False
        # 
        # pictureBox4
        # 
        self._pictureBox4.BackColor = System.Drawing.Color.Black
        self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._pictureBox4.Image = resources.GetObject("pictureBox4.Image")
        self._pictureBox4.Location = System.Drawing.Point(12, 297)
        self._pictureBox4.Name = "pictureBox4"
        self._pictureBox4.Size = System.Drawing.Size(682, 282)
        self._pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage
        self._pictureBox4.TabIndex = 20
        self._pictureBox4.TabStop = False
        # 
        # timer1
        # 
        self._timer1.Tick += self.Timer1Tick
        # 
        # pictureBox12
        # 
        self._pictureBox12.BackColor = System.Drawing.Color.Black
        self._pictureBox12.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._pictureBox12.Image = resources.GetObject("pictureBox12.Image")
        self._pictureBox12.Location = System.Drawing.Point(22, 297)
        self._pictureBox12.Name = "pictureBox12"
        self._pictureBox12.Size = System.Drawing.Size(602, 282)
        self._pictureBox12.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage
        self._pictureBox12.TabIndex = 21
        self._pictureBox12.TabStop = False
        self._pictureBox12.Visible = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(972, 655)
        self.Controls.Add(self._pictureBox12)
        self.Controls.Add(self._pictureBox11)
        self.Controls.Add(self._pictureBox10)
        self.Controls.Add(self._pictureBox9)
        self.Controls.Add(self._pictureBox7)
        self.Controls.Add(self._pictureBox8)
        self.Controls.Add(self._pictureBox6)
        self.Controls.Add(self._pictureBox5)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._progressBar1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._pictureBox3)
        self.Controls.Add(self._pictureBox2)
        self.Controls.Add(self._pictureBox1)
        self.Controls.Add(self._pictureBox4)
        self.Name = "MainForm"
        self.Text = "SlotMachine"
        self._pictureBox1.EndInit()
        self._pictureBox2.EndInit()
        self._pictureBox3.EndInit()
        self._pictureBox5.EndInit()
        self._pictureBox6.EndInit()
        self._pictureBox7.EndInit()
        self._pictureBox8.EndInit()
        self._pictureBox9.EndInit()
        self._pictureBox10.EndInit()
        self._pictureBox11.EndInit()
        self._pictureBox4.EndInit()
        self._pictureBox12.EndInit()
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label2Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        rnd = System.Random()
        money = rnd.Next(1,51)
        if money > 25:
            MessageBox.Show("YOU GOT CAUGHT! $10 BAIL FEE!!!")
            cmoney = float(self._label2.Text)
            cmoney -= 10
            self._label2.Text = str(round(cmoney, 2))
        else:
            cmoney = float(self._label2.Text)
            self._label2.Text = str(round(cmoney + money, 2))
        
        pass

    def Button1Click(self, sender, e):
        im1 = self._pictureBox5.BackgroundImage
        im2 = self._pictureBox6.BackgroundImage
        im3 = self._pictureBox7.BackgroundImage
        im4 = self._pictureBox8.BackgroundImage
        im5 = self._pictureBox9.BackgroundImage
        levOff = self._pictureBox10.BackgroundImage
        levOn = self._pictureBox11.BackgroundImage
        rnd = System.Random()

        # Copy above into timerTick
        pass
    
        if self._textBox1.Text == "":
            MessageBox.Show("You must enter an amount to bet first!")
            return
        
        money = float(self._label2.Text)
        bet = float(self._textBox1.Text)
        newmoney = money - bet
        
        if money <= 0:
            MessageBox.Show("You have no money!")
        elif bet < 1:
            MessageBox.Show("You must bet at least 1 dollar!")
        elif bet > money and bet > newmoney:
            MessageBox.Show("You don't have enough money!")
        else:
            self._button1.BackgroundImage = levOn
            self._button1.Enabled = False
            self._pictureBox4.Visible = True
            self._pictureBox12.Visible = True
            self._timer1.Enabled = True
            self._timer1.Enabled =  True
            self._progressBar1.Value = 0
            self._label2.Text = str(round(newmoney, 2))
            
            num1 = self.num1
            num2 = self.num2
            num3 = self.num3
            
            if num1 == 1 and num2 == 1 and num3 == 1:
                newmoney += bet * 2
            if num1 == num2 == num3 == 2:
                newmoney += bet * 3
            if num1 == num2 == num3 == 3:
                newmoney += bet * 5
            if num1 == num2 == num3 == 4:
                newmoney += bet * 25
            if num1 == num2 == num3 == 5:
                newmoney += bet * 100
            
            self.num1 = 0
            self.num2 = 0
            self.num3 = 0
            self._label2.Text = str(round(newmoney, 2))
            
            if newmoney <= 0:
                MessageBox.Show("You ran out of cash ),:")
            pass
            
            
            
        pass

    def Timer1Tick(self, sender, e):
        im1 = self._pictureBox5.BackgroundImage
        im2 = self._pictureBox6.BackgroundImage
        im3 = self._pictureBox7.BackgroundImage
        im4 = self._pictureBox8.BackgroundImage
        im5 = self._pictureBox9.BackgroundImage
        levOff = self._pictureBox10.BackgroundImage
        levOn = self._pictureBox11.BackgroundImage
        rnd = System.Random()
        
        images = [im1, im2, im3, im4, im5]
        for lcv in range(0,1000):
            self.num1 = rnd.Next(1,6) # generate a # between 1 and 5
            self.num2 = rnd.Next(1,6)
            self.num3 = rnd.Next(1,6)
            
            self._pictureBox1.BackgroundImage = images[self.num1 - 1]
            self._pictureBox2.BackgroundImage = images[self.num2 - 1]
            self._pictureBox3.BackgroundImage = images[self.num3 - 1]
            self._progressBar1.Increment(1)
            if self._progressBar1.Value == self._progressBar1.Maximum:
                self._timer1.Enabled = False
                self._button1.BackgroundImage = levOff
                self._button1.Enabled = True
                self._pictureBox12.Visible = False
                