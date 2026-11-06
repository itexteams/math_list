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


def bt_dang8_p3_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng màu từ 6 đến 9 để bài toán luôn có nghiệm ở tất cả các trường hợp
                m = random.randint(6, 9)

                # Hàm tính chỉnh hợp A(n, k)
                def A(n, k):
                    if k > n: return 0
                    res = 1
                    for i in range(k):
                        res *= (n - i)
                    return res

                # Tính toán các trường hợp (TH)
                th1 = A(m, 3)
                th2_val = A(m, 4)
                th2 = 3 * th2_val
                th3_val = A(m, 5)
                th3 = 3 * th3_val
                th4 = A(m, 6)

                kq = th1 + th2 + th3 + th4
                while kq>9999:
                    m = random.randint(6, 9)

                    # Hàm tính chỉnh hợp A(n, k)
                    def A(n, k):
                        if k > n: return 0
                        res = 1
                        for i in range(k):
                            res *= (n - i)
                        return res

                    # Tính toán các trường hợp (TH)
                    th1 = A(m, 3)
                    th2_val = A(m, 4)
                    th2 = 3 * th2_val
                    th3_val = A(m, 5)
                    th3 = 3 * th3_val
                    th4 = A(m, 6)

                    kq = th1 + th2 + th3 + th4
                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo danh sách các đáp án nhiễu có logic sai lầm phổ biến hoặc cộng/trừ sai lệch
                s = [
                    '$%s$' % (kq + 120),
                    '$%s$' % (kq - 120),
                    '$%s$' % (kq + 240),
                    '$%s$' % (kq - 240),
                    '$%s$' % (kq + 360),
                    '$%s$' % (kq - 360),
                    '$%s$' % (kq + 720),
                    '$%s$' % (th1 + th2_val + th3_val + th4), # Quên nhân 3 ở TH2 và TH3
                    '$%s$' % (m**6),                         # Tô tự do 6 đỉnh
                    '$%s$' % (th4),                          # Chỉ tính trường hợp 6 đỉnh khác màu
                ]

                # Loại bỏ các đáp án trùng lặp và trùng với đáp án đúng
                s_unique = []
                for item in s:
                    if item not in s_unique and item != '$%s$' % (kq):
                        s_unique.append(item)

                das1 = random.choice(s_unique)
                s_unique.remove(das1)
                das2 = random.choice(s_unique)
                s_unique.remove(das2)
                das3 = random.choice(s_unique)
                hinhve=r'''\scalebox{0.6}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]  (305.96,188.11) -- (227.38,231.99) -- (150.09,185.88) -- (151.38,95.89) -- (229.95,52.01) -- (307.24,98.12) -- cycle ;
            	\draw [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (229.95,52.01) -- (150.09,185.88) ;
            	\draw [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (229.95,52.01) -- (305.96,188.11) ;
            	\draw [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (305.96,188.11) -- (150.09,185.88) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (307.24,98.12) -- (151.38,95.89) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (307.24,98.12) -- (227.38,231.99) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (151.38,95.89) -- (227.38,231.99) ;
            	\draw  [fill={rgb, 255:red, 251; green, 6; blue, 35 }  ,fill opacity=1 ] (134.04,95.89) .. controls (134.04,86.32) and (141.8,78.56) .. (151.38,78.56) .. controls (160.95,78.56) and (168.71,86.32) .. (168.71,95.89) .. controls (168.71,105.46) and (160.95,113.22) .. (151.38,113.22) .. controls (141.8,113.22) and (134.04,105.46) .. (134.04,95.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (212.62,52.01) .. controls (212.62,42.44) and (220.38,34.68) .. (229.95,34.68) .. controls (239.53,34.68) and (247.29,42.44) .. (247.29,52.01) .. controls (247.29,61.58) and (239.53,69.34) .. (229.95,69.34) .. controls (220.38,69.34) and (212.62,61.58) .. (212.62,52.01) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (289.91,98.12) .. controls (289.91,88.55) and (297.67,80.79) .. (307.24,80.79) .. controls (316.82,80.79) and (324.58,88.55) .. (324.58,98.12) .. controls (324.58,107.69) and (316.82,115.45) .. (307.24,115.45) .. controls (297.67,115.45) and (289.91,107.69) .. (289.91,98.12) -- cycle ;
            	\draw  [fill={rgb, 255:red, 144; green, 19; blue, 254 }  ,fill opacity=1 ] (288.62,188.11) .. controls (288.62,178.54) and (296.38,170.78) .. (305.96,170.78) .. controls (315.53,170.78) and (323.29,178.54) .. (323.29,188.11) .. controls (323.29,197.68) and (315.53,205.44) .. (305.96,205.44) .. controls (296.38,205.44) and (288.62,197.68) .. (288.62,188.11) -- cycle ;
            	\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (210.05,231.99) .. controls (210.05,222.42) and (217.81,214.66) .. (227.38,214.66) .. controls (236.95,214.66) and (244.71,222.42) .. (244.71,231.99) .. controls (244.71,241.56) and (236.95,249.32) .. (227.38,249.32) .. controls (217.81,249.32) and (210.05,241.56) .. (210.05,231.99) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (132.76,185.88) .. controls (132.76,176.31) and (140.52,168.55) .. (150.09,168.55) .. controls (159.66,168.55) and (167.42,176.31) .. (167.42,185.88) .. controls (167.42,195.45) and (159.66,203.21) .. (150.09,203.21) .. controls (140.52,203.21) and (132.76,195.45) .. (132.76,185.88) -- cycle ;
            	\draw (142,87) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (221.33,44) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (299,91) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (297.33,180) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (218,225) node [anchor=north west][inner sep=0.75pt]    {$E$};
            	\draw (141.33,177) node [anchor=north west][inner sep=0.75pt]    {$F$};
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Bạn An có một hộp bút màu gồm $%s$ màu khác nhau. Bạn muốn dùng các bút màu này để tô màu cho $6$ hình tròn nằm trên các đỉnh của một lục giác đều $ABCDEF$. Bên trong lục giác đều này có thêm các đường thẳng nối với nhau tạo thành hai tam giác đều $ACE$ và $BDF$ (như hình vẽ). Biết rằng khi tô màu thì hai đỉnh bất kỳ có đường nối trực tiếp với nhau thì không được tô cùng màu (màu sắc ở các đỉnh không kề nhau có thể được lặp lại). Hỏi bạn An có tất cả bao nhiêu cách để tô màu cho các hình tròn đó?}{%s}''' 
                                 % (m, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Dựa vào hình vẽ, các đường thẳng tạo thành các kết nối giữa các đỉnh. Hai đỉnh bất kỳ có đường nối trực tiếp thì không được cùng màu. Ta thấy các đỉnh của lục giác đều được chia thành $3$ cặp đỉnh đối diện không có đường nối trực tiếp với nhau: $\\left( A,D \\right)$, $\\left( B,E \\right)$, $\\left( C,F \\right)$.\\\\
                Mọi đỉnh trong một cặp đều có đường nối trực tiếp đến tất cả $4$ đỉnh của $2$ cặp còn lại (ví dụ $A$ nối với $B,C,E,F$).\\\\
                Do đó, để thỏa mãn điều kiện bài toán, tập màu được tô cho mỗi cặp phải hoàn toàn phân biệt nhau.\\\\
                Với mỗi cặp đỉnh không kề nhau, ta có thể tô bằng $1$ màu (nếu $2$ đỉnh tô cùng màu) hoặc $2$ màu (nếu $2$ đỉnh tô khác màu).\\\\
                Ta chia thành các trường hợp sau dựa trên số cặp đỉnh được tô cùng màu:\\\\
                + Trường hợp 1: Cả $3$ cặp đỉnh đều được tô cùng màu (mỗi cặp $1$ màu). Ta cần chọn $3$ màu từ $%s$ màu và phân cho $3$ cặp. Số cách tô là $A_{%s}^{3} = %s$.\\\\
                + Trường hợp 2: Có $2$ cặp đỉnh tô cùng màu, $1$ cặp đỉnh tô khác màu. Có $C_{3}^{1} = 3$ cách chọn cặp đỉnh tô khác màu. Khi đó ta cần chọn $4$ màu từ $%s$ màu và xếp vào $4$ vị trí (gồm $2$ vị trí là $2$ cặp cùng màu, $2$ vị trí là $2$ đỉnh của cặp khác màu). Số cách tô là $3 \\cdot A_{%s}^{4} = 3 \\cdot %s = %s$.\\\\
                + Trường hợp 3: Có $1$ cặp đỉnh tô cùng màu, $2$ cặp đỉnh tô khác màu. Có $C_{3}^{1} = 3$ cách chọn cặp đỉnh tô cùng màu. Ta cần chọn $5$ màu từ $%s$ màu và xếp vào $5$ vị trí. Số cách tô là $3 \\cdot A_{%s}^{5} = 3 \\cdot %s = %s$.\\\\
                + Trường hợp 4: Cả $3$ cặp đỉnh đều tô khác màu. Ta cần chọn $6$ màu từ $%s$ màu và xếp vào $6$ vị trí. Số cách tô là $A_{%s}^{6} = %s$.\\\\
                Tổng số cách tô màu là: $%s + %s + %s + %s = %s$ (cách).''' 
                           % (m, m, th1, m, m, th2_val, th2, m, m, th3_val, th3, m, m, th4, th1, th2, th3, th4, kq))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

