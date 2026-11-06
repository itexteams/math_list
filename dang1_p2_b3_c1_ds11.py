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


def bt_dang1_p2_b3_c1_ds11(self):
            # Khai báo biến
            a = randint(1,4)
            b = randint(-4,-1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho đồ thị hàm số $y=%s \\sin x$.''' #5
                            '\\begin{center} \n'
                            '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                '	\\draw[->] (-7.5,0)--(7.5,0) node[below left] {$x$};    \n' 
                                '	\\draw[->] (0,-%s.5)--(0,%s.5) node[below left] {$y$};   \n' #4
                                '	\\clip(-8.5,-%s.5) rectangle (8.5,%s.5); \n' #8
                                '	\\draw[line width=1.pt,smooth,samples=100,domain=-6.944831115747839:7.276459369685686] plot(\\x,{%s*sin(((\\x))*180/pi)});  \n' #1
                                '	\\draw [line width=1.pt,dash pattern=on 2pt off 2pt,domain=-6.944831115747839:7.276459369685686] plot(\\x,{(%s.-0.*\\x)/1.});  \n' #6
                                '	\\draw [line width=1.pt,dash pattern=on 2pt off 2pt,domain=-6.944831115747839:7.276459369685686] plot(\\x,{(%s.-0.*\\x)/1.});  \n' #7
                                '	\\draw (0.006258184937230426,0.16723577357305897) node[anchor=north west] {$O$};  \n'
                                '	\\draw (1.3659522996420943,-0.040880672555236586) node[anchor=north west] {$\\frac{\\pi}{2}$};  \n'
                                '	\\draw (2.7337628604752535,0.0146170464123089) node[anchor=north west] {$\\pi$};  \n'
                                '	\\draw (4.413921988155294,0.9418127687517859) node[anchor=north west] {$\\frac{3\\pi}{2}$};  \n'
                                '	\\draw (6.138756130851004,0.02849147615419527) node[anchor=north west] {$2\\pi$};  \n'
                                '	\\draw (-1.9777852681525199,1.0135759878281276) node[anchor=north west] {$-\\frac{\\pi}{2}$};  \n'
                                '	\\draw (-3.7178469695019063,0.02849147615419527) node[anchor=north west] {$-\\pi$};  \n'
                                '	\\draw (-5.168904108786384,-0.027006242813350213) node[anchor=north west] {$-\\frac{3\\pi}{2}$};  \n'
                                '	\\draw (-7.112185159055512,0.6735037759942117) node[anchor=north west] {$-2\\pi$};  \n'
                                '	\\draw (-0.49322128577067875,%s) node[anchor=north west] {$%s$};  \n' #2
                                '	\\draw (-0.8539564590597243,%s) node[anchor=north west] {$%s$};  \n' #3
                                '	\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-4.71238898038469,%s.)-- (-4.71238898038469,0.);  \n' #11
                                '	\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-1.5707963267948966,0.)-- (-1.5707963267948966,-%s.);  \n' #12
                                '	\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.5707963267948966,%s.)-- (1.5707963267948966,0.);  \n' #13
                                '	\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (4.71238898038469,0.)-- (4.71238898038469,-%s.);  \n' #14
                                '\\end{tikzpicture} } \n'
                            '\\end{center}'
                            %(latex(a), #5
                                latex(a),latex(a), #4
                                latex(a+1),latex(a+1),
                                latex(a),#1
                                latex(a), #6
                                latex(-a), #7
                            latex(a),latex(a),#2
                            latex(-a),latex(-a),#3
                            latex(a), #11
                            latex(a), #12
                            latex(a), #13
                            latex(a), #14
                            ))


            # Các đáp án
            da_1_d = '\\True Hàm số đồng biến trên khoảng $\\left(-\\dfrac{\\pi}{2};\\dfrac{\\pi}{2} \\right)$'
            da_1_s = 'Hàm số nghịch biến trên khoảng $\\left(-\\dfrac{\\pi}{2};\\dfrac{\\pi}{2} \\right)$'
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Hàm số nghịch biến trên khoảng $\\left(\\dfrac{\\pi}{2};\\dfrac{3\\pi}{2} \\right)$'
            da_2_s = 'Hàm số đồng biến trên khoảng $\\left(\\dfrac{\\pi}{2};\\dfrac{3\\pi}{2} \\right)$'
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Hàm số có giá trị lớn nhất là $%s$' %(latex(a))
            da_3_s = 'Hàm số có giá trị lớn nhất là $%s$' %(latex(a-1))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Hàm số có giá trị nhỏ nhất là $%s$' %(latex(-a))
            da_4_s = 'Hàm số có giá trị nhỏ nhất là $%s$' %(latex(-a+1))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Chu kỳ của hàm số là $2\\pi$'
            da_5_s = 'Chu kỳ của hàm số là $\\pi$'
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Trên khoảng $(-2\\pi;2\\pi)$, đồ thị hàm số cắt đường thẳng $y=%s$ tại $4$ điểm phân biệt'%(latex(b))
            da_6_s = 'Trên khoảng $(-2\\pi;2\\pi)$, đồ thị hàm số cắt đường thẳng $y=%s$ tại $3$ điểm phân biệt'%(latex(b))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Đồ thị hàm số đối xứng qua góc tọa độ'
            da_7_s = 'Đồ thị hàm số đối xứng qua trục $Oy$'
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            da_8_d = '\\True Hàm số đã cho là hàm số lẻ'
            da_8_s = 'Hàm số đã cho là hàm số chẵn'
            list_da_8=[da_8_d,da_8_s]
            da_8=random.choice(list_da_8)

            da_9_d = '\\True Hàm số nhận giá trị dương trên khoảng $(-2\\pi;-\\pi)$'
            da_9_s = 'Hàm số nhận giá trị âm trên khoảng $(-2\\pi;-\\pi)$'
            list_da_9=[da_9_d,da_9_s]
            da_9=random.choice(list_da_9)

            da_10_d = '\\True Hàm số nhận giá trị âm trên khoảng $(\\pi;2\\pi)$'
            da_10_s = 'Hàm số nhận giá trị dương trên khoảng $(\\pi;2\\pi)$'
            list_da_10=[da_10_d,da_10_s]
            da_10=random.choice(list_da_10)

            da_11_d = '\\True Có $3$ điểm trên đoạn $\\left[-\\dfrac{3\\pi}{2};\\dfrac{3\\pi}{2} \\right]$ để hàm số nhận giá trị bằng $0$'
            da_11_s = 'Có $4$ điểm trên đoạn $\\left[-\\dfrac{3\\pi}{2};\\dfrac{3\\pi}{2} \\right]$ để hàm số nhận giá trị bằng $0$'
            list_da_11=[da_11_d,da_11_s]
            da_11=random.choice(list_da_11)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7, da_8, da_9, da_10, da_11]

            # Nội dung lời giải
            loigiai_1 = ('Đồ thị hàm số đi lên trên khoảng $\\left(-\\dfrac{\\pi}{2};\\dfrac{\\pi}{2} \\right)$. \n'
                        'Do đó, hàm số đồng biến trên khoảng $\\left(-\\dfrac{\\pi}{2};\\dfrac{\\pi}{2} \\right)$.'
                        )
            loigiai_2 = ('Từ trái sang phải đồ thị hàm số đi xuống trên khoảng $\\left(\\dfrac{\\pi}{2};\\dfrac{3\\pi}{2} \\right)$. \n'
                        'Do đó, hàm số nghịch biến trên khoảng $\\left(\\dfrac{\\pi}{2};\\dfrac{3\\pi}{2} \\right)$.'
                        )
            loigiai_3 = ('Từ đồ thị ta thấy hàm số có giá trị lớn nhất là $%s$.'
                        %(latex(a))
                        )
            loigiai_4 = ('Từ đồ thị ta thấy hàm số có giá trị nhỏ nhất là $%s$.'
                        %(latex(-a))
                        )
            loigiai_5 = ('Chu kỳ của hàm số là $2\\pi$.'

                        )
            loigiai_6 = ('Trên khoảng $(-2\\pi;2\\pi)$, đồ thị hàm số cắt đường thẳng $y=%s$ tại $4$ điểm phân biệt.'
                        %(latex(b))
                        )
            loigiai_7 = ('Đồ thị hàm số đối xứng qua góc tọa độ.'
                        )

            loigiai_8 = ('Từ đồ thị ta thấy $f(-x)=-f(x)$ nên hàm số là hàm lẻ.'
                        )

            loigiai_9 = ('Hàm số nhận giá trị dương trên khoảng $(-2\\pi;-\\pi)$.'
                        )

            loigiai_10 = ('Hàm số nhận giá trị âm trên khoảng $(\\pi;2\\pi)$.'
                        )

            loigiai_11 = ('Hàm số nhận giá trị bằng $0$ tại giao điểm của đồ thị hàm số với trục $Ox$. \n'
                        'Do đó, có $3$ điểm trên đoạn $\\left[-\\dfrac{3\\pi}{2};\\dfrac{3\\pi}{2} \\right]$ để hàm số nhận giá trị bằng $0$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7, loigiai_8, loigiai_9, loigiai_10, loigiai_11]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined = list(zip(list_1, list_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers, shuffled_solutions = zip(*combined)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('1 \\sin x', '\\sin x')
            return content

