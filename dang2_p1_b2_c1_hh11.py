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


def bt_dang2_p1_b2_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12',]
            dang=random.choice(lisdang)
            hinhve = ('\\begin{center}\n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.4244394472247963,-0.745609730923229) rectangle (5.842639990831729,5.682413568492722);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,2.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (5.,2.);\n'
            '\\draw (5.,2.)-- (3.,0.);\n'
            '\\draw (3.,0.)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (2.,5.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (2.,2.);\n'
            '\\draw (2.,5.)-- (3.,0.);\n'
            '\\draw (2.,5.)-- (5.,2.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,3.5)-- (3.5,3.5);\n'
            '\\draw (3.5,3.5)-- (2.5,2.5);\n'
            '\\draw (2.5,2.5)-- (1.,2.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,2.5)-- (2.,3.5);\n'
            '\\draw (1.803793492968611,5.6) node[anchor=north west] {$S$};\n'
            '\\draw (-0.3,0) node[anchor=north west] {$B$};\n'
            '\\draw (1.8,2) node[anchor=north west] {$A$};\n'
            '\\draw (5,2.3) node[anchor=north west] {$D$};\n'
            '\\draw (2.77084124597809,0.03656124577561453) node[anchor=north west] {$C$};\n'
            '\\draw (0.5665412207358954,2.866598052376885) node[anchor=north west] {$J$};\n'
            '\\draw (1.5335889737453743,4.004301291211567) node[anchor=north west] {$I$};\n'
            '\\draw (3.5814548036478,3.9616374197552657) node[anchor=north west] {$F$};\n'
            '\\draw (2.6286283411237545,2.866598052376885) node[anchor=north west] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n')

            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [

                    '$EF$',
                    '$CD$',
                    '$AB$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$.\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I, J, E, F$ lần lượt là trung điểm của các cạnh $SA, SB, SC$ và $SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào song song với $IJ$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='2':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [

                    '$IJ$',
                    '$CD$',
                    '$EF$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$.\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào song song với $AB$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='3':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [

                    '$IJ$',
                    '$AB$',
                    '$EF$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$.\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào song song với $CD$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='4':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [

                    '$IJ$',
                    '$AB$',
                    '$CD$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$.\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào song song với $EF$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='5':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$EF$',
                    '$CD$',
                    '$AB$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào \\textbf{không} song song với $IJ$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='6':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$IJ$',
                    '$CD$',
                    '$AB$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào \\textbf{không} song song với $EF$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='7':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$EF$',
                    '$CD$',
                    '$IJ$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào \\textbf{không} song song với $AB$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='8':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$FD$',
                    '$AD$',
                    '$BC$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IJ là đường trung bình trong tam giác $SAB$ nên $\\heva{& IJ //AB \\\\& IJ=\\dfrac{1}{2}AB}$\\\\ \n'
                    'Tương tự vì EF là đường trung bình trong tam giác $SAB$ nên $\\heva{& EF //CD \\\\& EF=\\dfrac{1}{2}CD}$\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AB$//$CD$\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IJ//EF//AB//CD$.\\\\ \n'),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$EF$',
                    '$IJ$',
                    '$AB$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào \\textbf{không} song song với $CD$? \n')
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]


            if dang=='9':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [

                    '$EJ$',
                    '$AD$',
                    '$BC$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IF là đường trung bình trong tam giác $SAD$ nên $\\heva{& IF //AD \\\\& IF=\\dfrac{1}{2}AD}$.\\\\ \n'
                    'Tương tự vì EJ là đường trung bình trong tam giác $SBC$ nên $\\heva{& EJ //CB \\\\& EJ=\\dfrac{1}{2}BC}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AD$//$BC$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IF//EJ//AD//BC$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$EC$',
                    '$JB$',
                    '$AB$',
                    '$CD$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào song song với $IF$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='10':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [

                    '$IF$',
                    '$AD$',
                    '$BC$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IF là đường trung bình trong tam giác $SAD$ nên $\\heva{& IF //AD \\\\& IF=\\dfrac{1}{2}AD}$.\\\\ \n'
                    'Tương tự vì EJ là đường trung bình trong tam giác $SBC$ nên $\\heva{& EJ //CB \\\\& EJ=\\dfrac{1}{2}BC}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AD$//$BC$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IF//EJ//AD//BC$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$SA$',
                    '$SB$',
                    '$SC$',
                    '$SD$',
                    '$AC$',
                    '$BD$',
                    '$FD$',
                    '$IA$',
                    '$AB$',
                    '$CD$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào song song với $EJ$? \n')

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='11':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [   '$SA$',
                        '$SB$',
                        '$SC$',
                        '$SD$',
                        '$AC$',
                        '$BD$',
                        '$FD$',
                        '$IA$',
                        '$AB$',
                        '$CD$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IF là đường trung bình trong tam giác $SAD$ nên $\\heva{& IF //AD \\\\& IF=\\dfrac{1}{2}AD}$.\\\\ \n'
                    'Tương tự vì EJ là đường trung bình trong tam giác $SBC$ nên $\\heva{& EJ //CB \\\\& EJ=\\dfrac{1}{2}BC}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AD$//$BC$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IF//EJ//AD//BC$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$IF$',
                    '$AD$',
                    '$BC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào \\textbf{không} song song với $EJ$? \n')
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            if dang=='12':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = [   '$SA$',
                        '$SB$',
                        '$SC$',
                        '$SD$',
                        '$AC$',
                        '$BD$',
                        '$FD$',
                        '$IA$',
                        '$AB$',
                        '$CD$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có vì IF là đường trung bình trong tam giác $SAD$ nên $\\heva{& IF //AD \\\\& IF=\\dfrac{1}{2}AD}$.\\\\ \n'
                    'Tương tự vì EJ là đường trung bình trong tam giác $SBC$ nên $\\heva{& EJ //CB \\\\& EJ=\\dfrac{1}{2}BC}$.\\\\ \n'
                    'Mặt khác $ABCD$ là hình bình hành nên $AD$//$BC$.\\\\ \n'
                    'Khi đó $IJEF$ là hình bình hành. Vậy $IF//EJ//AD//BC$.\\\\ \n'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = [
                    '$EJ$',
                    '$AD$',
                    '$BC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)


                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.'
                                ' Gọi $I,J,E,F$ lần lượt là trung điểm $SA,SB,SC,SD$. Trong các đường thẳng sau,'
                                ' đường thẳng nào \\textbf{không} song song với $IF$? \n')


                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(hinhve)+''+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

