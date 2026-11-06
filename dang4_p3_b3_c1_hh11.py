import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang4_p3_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)

            if dang=='4':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M, N, Q$ lần lượt là trung điểm các cạnh $AB, CD, SA$. Có tất cả bao nhiêu cạnh của hình chóp song song với mặt phẳng $(MNQ)$?  \n'
                                %(
                                ))

                # Nội dung lời giải
                loigiai = (
                            '\\begin{center} \n'
                                '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm] \n'
                                    '\\clip(-0.8520253137941977,-0.6506683108054448) rectangle (6.810933261647972,5.927170583150741); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,2.); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (6.,2.); \n'
                                    '\\draw (6.,2.)-- (4.,0.); \n'
                                    '\\draw (4.,0.)-- (0.,0.); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3.,5.)-- (2.,2.); \n'
                                    '\\draw (3.,5.)-- (0.,0.); \n'
                                    '\\draw (3.,5.)-- (4.,0.); \n'
                                    '\\draw (3.,5.)-- (6.,2.); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (1.,1.)-- (5.,1.); \n'
                                    '\\draw (5.,1.)-- (4.464254940928736,3.535745059071264); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (4.464254940928736,3.535745059071264)-- (2.5070040145836803,3.5210120437510404); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2.5070040145836803,3.5210120437510404)-- (1.,1.); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2.5070040145836803,3.5210120437510404)-- (3.,1.); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2.5070040145836803,3.5210120437510404)-- (5.,1.); \n'
                                    '\\draw (2.75,5.5) node[anchor=north west] {S}; \n'
                                    '\\draw (2,2.5) node[anchor=north west] {A}; \n'
                                    '\\draw (-0.6,0.14359454883892456) node[anchor=north west] {B}; \n'
                                    '\\draw (3.7,0) node[anchor=north west] {C}; \n'
                                    '\\draw (6,2.3) node[anchor=north west] {D}; \n'
                                    '\\draw (2.65,1) node[anchor=north west] {O}; \n'
                                    '\\draw (0.7029400029743595,1) node[anchor=north west] {M}; \n'
                                    '\\draw (5,1) node[anchor=north west] {N}; \n'
                                    '\\draw (4.540012691115475,3.9) node[anchor=north west] {P}; \n'
                                    '\\draw (2,3.8) node[anchor=north west] {Q}; \n'
                                '\\end{tikzpicture} \n'
                            '\\end{center} \n'

                        'Ta có 3 cạnh của hình chóp là $AB, CD, SA$ đều có điểm chung với mặt phẳng $(MNQ)$ nên không thể song song với mặt phẳng này. \\\\ \n'
                        'Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$, và $P$ là trung điểm của $SD$.\\\\ \n'
                        'Ta có $BC//MN//AD$ nên $BC$ và $AD$ đều song song với mặt phẳng $(MNQ)$.\\\\ \n'
                        'Ta lại có $SB//MQ \\Rightarrow SB//(MNQ)$ và $SC//OQ\\Rightarrow SC//(MNQ)$. \\\\ \n'
                        'Vì $SD$ cắt mặt phẳng $(MNQ)$ tại trung điểm $P$ của $SD$. \\\\ \n'
                        'Vậy có tất cả $4$ cạnh của hình chóp song song với mặt phẳng $(MNQ)$. \\\\ \n'

                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(4))   

            if dang=='3':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $G_1, G_2$ lần lượt là trọng tâm tam giác $BCD$ và $ACD$. Khi đó đoạn thẳng $G_1 G_2$ song song với bao nhiêu mặt của tứ diện $ABCD$?  \n'
                                %(
                                ))

                # Nội dung lời giải
                loigiai = (
                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm] \n'
                                '\\clip(-0.593381104547192,-2.696905511232099) rectangle (5.696167691189903,4.437667697537691); \n'
                                '\\draw (0.,0.)-- (4.,-2.); \n'
                                '\\draw (4.,-2.)-- (5.,0.); \n'
                                '\\draw (0.,0.)-- (2.,4.); \n'
                                '\\draw (2.,4.)-- (4.,-2.); \n'
                                '\\draw (5.,0.)-- (2.,4.); \n'
                                '\\draw (2.,4.)-- (2.0005310244043546,-1.0002655122021773); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.0005310244043546,-1.0002655122021773)-- (5.,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.000313941893605,1.043840526807085)-- (3.075094043647561,-0.641919305729621); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.); \n'
                                '\\draw (1.7,4.6) node[anchor=north west] {A}; \n'
                                '\\draw (5,0.2) node[anchor=north west] {B}; \n'
                                '\\draw (-0.5,0.2) node[anchor=north west] {C}; \n'
                                '\\draw (3.931243284222861,-1.9374531906584032) node[anchor=north west] {D}; \n'
                                '\\draw (1.3,-0.8) node[anchor=north west] {M}; \n'
                                '\\draw (2.9899502671737723,-0.5896927344290277) node[anchor=north west] {$G_1$}; \n'
                                '\\draw (1.3,1.5) node[anchor=north west] {$G_2$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                        'Gọi $M$ là trung điểm của $CD$. \\\\ \n'
                        'Xét tam giác $ABM$ có \\\\ \n'
                        '\\hspace*{1cm} $\\heva{& \\frac{MG_2}{AM} = \\frac{1}{3} \\\\& \\frac{MG_1}{BM} = \\frac{1}{3}} \\Rightarrow G_1G_2 // AB$. \\\\ \n'
                        'Mà \\\\ \n'
                        '\\hspace*{1cm} $\\heva{& AB \\subset (ABC) \\Rightarrow G_1G_2 // (ABC) \\\\& AB \\subset (ABD) \\Rightarrow G_1G_2 // (ABD) }$.\\\\ \n'
                        'Vậy $G_1 G_2$ song song với $2$ mặt của tứ diện $ABCD$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(2))

            if dang=='2':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trọng tâm các tam giác $ABC$ và $ABD$. Đường thẳng $MN$ song song với bao nhiêu mặt phẳng trong bốn mặt của tứ diện? \n'
                                %(
                                ))

                # Nội dung lời giải
                loigiai = (
                        '\\begin{center}  \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.9406042311374152,-2.7942745283015604) rectangle (5.88293527616247,3.772177148268006); \n'
                                '\\draw (0.,0.)-- (3.397752912436294,-2.0444350220048726); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.); \n'
                                '\\draw (5.,0.)-- (3.397752912436294,-2.0444350220048726); \n'
                                '\\draw (0.,0.)-- (3.0121211663408536,3.011625649024223); \n'
                                '\\draw (3.0121211663408536,3.011625649024223)-- (3.397752912436294,-2.0444350220048726); \n'
                                '\\draw (3.0121211663408536,3.011625649024223)-- (5.,0.); \n'
                                '\\draw (2.7,3.5) node[anchor=north west] {A}; \n' 
                                '\\draw (-0.6,0.4) node[anchor=north west] {B}; \n' 
                                '\\draw (3.2,-2.1) node[anchor=north west] {C}; \n' 
                                '\\draw (4.9,0.4) node[anchor=north west] {D}; \n'
                                '\\draw (1.5,0.9) node[anchor=north west] {M}; \n'
                                '\\draw (2.4,1.5) node[anchor=north west] {N}; \n'
                                '\\draw (3.0121211663408536,3.011625649024223)-- (1.5630537004748122,-0.9404926752704048); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (3.0121211663408536,3.011625649024223)-- (2.797881307398942,0.); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.797881307398942,0.)-- (1.5630537004748122,-0.9404926752704048); \n'
                                '\\draw [dash pattern=on 2pt off 2pt] (2.8809576017656493,1.1678251665041464)-- (2.152005138210435,0.6657857237850302); \n'
                                '\\draw (1,-0.9) node[anchor=north west] {E}; \n'
                                '\\draw (2.6,-0) node[anchor=north west] {F}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                        'Gọi $E, F$ lần lượt là trung điểm của $BC$ và $BD$. \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\dfrac{AM}{AE} = \\dfrac{AN}{AF} = \\dfrac{2}{3} \\Rightarrow MN // EF$, mà $EF \\subset (BCD)$ suy ra $MN // (BCD)$. \\\\ \n'
                        'Ta lại có $MN // EF$ và $EF // CD$ suy ra $MN // CD$ do đó $MN // (ACD)$. \\\\ \n'
                        '$MN$ cắt $(ABC)$ tại $M$ và cắt mặt phẳng $(ABD)$ tại $N$, nên $MN$ không song song với hai mặt phẳng này. \\\\ \n'
                        'Vậy đường thẳng $MN$ song song với $2$ mặt phẳng trong bốn mặt của tứ diện.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(2))

            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AD, P$ là điểm trên cạnh $AC$ sao cho $PA = 2PC$. Trong ba đường thẳng $MN, NP, PM$ có bao nhiêu đường thẳng song song với mặt phẳng $(BCD)$?  \n'
                                %(
                                ))

                # Nội dung lời giải
                loigiai = (
                            '\\begin{center}    \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]    \n'
                            '\\clip(-0.6192444427245478,-2.5) rectangle (5.990055205633425,3.686481204691242); \n'
                            '\\draw (0.,0.)-- (3.,-2.); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw (5.,0.)-- (3.,-2.); \n'
                            '\\draw (0.,0.)-- (3.,3.); \n'
                            '\\draw (3.,3.)-- (3.,-2.); \n'
                            '\\draw (3.,3.)-- (5.,0.); \n'
                            '\\draw (2.7,3.5) node[anchor=north west] {A}; \n'
                            '\\draw (-0.6,0.4) node[anchor=north west] {B}; \n'
                            '\\draw (2.7,-1.9) node[anchor=north west] {C}; \n'
                            '\\draw (4.9,0.4) node[anchor=north west] {D}; \n'
                            '\\draw (0.8,1.8) node[anchor=north west] {M}; \n'
                            '\\draw (4,1.8) node[anchor=north west] {N}; \n'
                            '\\draw (2.5,-0.3) node[anchor=north west] {P}; \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (1.4211424550388474,1.4211424550388474)-- (4.074507196932682,1.3882392046009766); \n'
                            '\\draw (4.074507196932682,1.3882392046009766)-- (3.,-0.40550010109925516); \n'
                            '\\draw (3.,-0.40550010109925516)-- (1.4211424550388474,1.4211424550388474); \n'
                        '\\end{tikzpicture}   \n'
                        '\\end{center}  \n'

                        'Ta có $\\heva{& MN // BD \\\\& BD \\subset (BCD) } \\Rightarrow MN // (BCD)$. \\\\ \n'
                        'Trong $(ABC)$, hai đường thẳng phân biệt $MP$ và $BC$ không song song nên cắt nhau tại một điểm, do đó $MP$ có điểm chung với mặt phẳng $(BCD)$. \\\\ \n'
                        'Trong $(ACD)$, hai đường thẳng phân biệt $PN$ và $CD$ không song song nên cắt nhau tại một điểm, do đó $PN$ có điểm chung với mặt phẳng $(BCD)$. \\\\ \n'
                        'Vậy trong ba đường thẳng có $1$ đường song song với mặt phẳng $(BCD)$.'
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content     

