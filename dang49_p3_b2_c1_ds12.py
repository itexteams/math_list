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


def bt_dang49_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random khoảng cách BC (chọn số chẵn để h = BC/2 ra số nguyên)
                d_val = random.choice([10, 12, 14, 16, 18, 20, 24, 30, 40])
                d_sq = d_val ** 2

                # Tính kết quả đúng h = d/2
                kq = d_val // 2

                # Các đáp án trắc nghiệm
                da = str(kq)

                # Tạo các phương án nhiễu sai khác nhau
                s_set = set()
                while len(s_set) < 3:
                    offset = random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    wrong_val = kq + offset
                    if wrong_val > 0 and wrong_val != kq:
                        s_set.add(str(wrong_val))

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\scalebox{0.6}{  \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (273.87,179.55) -- (289.52,177.03) -- (290.53,234.05) -- (282.45,236.07) -- (274.38,233.55) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.17 ] (273.87,179.55) -- (279.87,180.8) -- (282.45,236.07) -- (274.38,233.55) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.29 ] (283.26,221.94) -- (363.5,270.39) -- (145.49,292.34) -- (62.42,240.11) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (82.61,154.82) -- (98.25,158.35) -- (79.07,241.12) -- (69.99,245.16) -- (62.42,240.11) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (66.96,130.6) -- (278.41,112.94) -- (278.41,120) -- (82.61,136.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (278.41,120) -- (360.67,156.34) -- (146.7,175.01) -- (82.61,136.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 71; green, 93; blue, 116 }  ,fill opacity=1 ] (131.13,142.03) .. controls (161.41,126.89) and (149.91,137.76) .. (170.5,142.03) .. controls (172.74,149.27) and (169.71,153.06) .. (170.61,156.52) .. controls (163.23,163.2) and (135.37,163.2) .. (131.68,155.33) .. controls (131.78,151.35) and (131.63,146.95) .. (131.13,142.03) -- cycle ;
            	\draw  [fill={rgb, 255:red, 28; green, 59; blue, 94 }  ,fill opacity=1 ] (131.13,142.03) .. controls (131.13,138) and (139.95,134.74) .. (150.82,134.74) .. controls (161.69,134.74) and (170.5,138) .. (170.5,142.03) .. controls (170.5,146.06) and (161.69,149.33) .. (150.82,149.33) .. controls (139.95,149.33) and (131.13,146.06) .. (131.13,142.03) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ][fill={rgb, 255:red, 244; green, 243; blue, 188 }  ,fill opacity=1 ] (135.39,72.06) .. controls (141.95,66.51) and (154.75,70.54) .. (165.65,74.18) .. controls (165.26,77.1) and (169.71,100.82) .. (162.9,108.39) .. controls (162.83,121.67) and (164.78,134.54) .. (166.18,142.21) .. controls (157.09,146.44) and (139.59,148.57) .. (135.9,140.69) .. controls (135.96,138.39) and (136.4,122.78) .. (135.65,106.12) .. controls (133.38,91.74) and (133.9,76.3) .. (135.39,72.06) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (151.81,35.41) .. controls (155.06,51.81) and (164.5,60.04) .. (152.06,68.02) .. controls (141.76,64.15) and (137.89,53.02) .. (151.81,35.41) -- cycle ;
            	\draw    (151.44,62.87) -- (150.74,75.09) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (278.41,112.94) -- (374.3,157.35) -- (358.15,155.33) -- (278.41,120) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (358.15,155.33) -- (374.3,157.35) -- (144.18,180.05) -- (146.7,175.01) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (82.61,136.15) -- (146.7,175.01) -- (144.18,180.05) -- (66.96,130.6) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 111; green, 70; blue, 34 }  ,fill opacity=1 ] (66.96,130.6) -- (144.18,180.05) -- (143.77,194.69) -- (66.46,145.74) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (283.97,197.21) -- (347.55,227.49) -- (348.56,237.08) -- (281.95,205.79) -- (279.93,199.23) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (82.1,202.76) -- (151.24,241.12) -- (148.21,251.21) -- (77.56,210.84) -- (78.06,204.78) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (340.99,167.94) -- (356.64,171.48) -- (359.66,272.1) -- (350.08,273.11) -- (342.51,270.59) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (152.25,224.87) -- (309.2,213.26) -- (315.25,215.78) -- (312.73,220.83) -- (153.26,232.44) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (147.2,187.62) -- (162.34,186.62) -- (156.79,286.54) -- (151.24,291.08) -- (140.14,288.56) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (144.18,180.05) -- (374.3,157.35) -- (373.29,170.97) -- (143.77,194.69) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.35 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (229.97,142.93) .. controls (229.97,139.34) and (236.64,136.44) .. (244.88,136.44) .. controls (253.12,136.44) and (259.79,139.34) .. (259.79,142.93) .. controls (259.79,146.52) and (253.12,149.42) .. (244.88,149.42) .. controls (236.64,149.42) and (229.97,146.52) .. (229.97,142.93) -- cycle ;
            	\draw    (155.03,155.48) -- (244.88,142.93) ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (155.03,155.48) -- (125.05,158.35) ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (151.81,35.41) -- (121.84,38.29) ;
            	\draw    (121.89,40.29) -- (124.99,156.36) ;
            	\draw [shift={(125.05,158.35)}, rotate = 268.47] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            	\draw [shift={(121.84,38.29)}, rotate = 88.47] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (244.88,142.93) -- (242.38,28.91) ;
            	\draw    (234.81,132.62) .. controls (236.33,124.29) and (243.9,126.56) .. (245.86,131.25) ;
            	\draw    (206.57,96.9) -- (244.88,142.93) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.12 ][fill={rgb, 255:red, 206; green, 224; blue, 242 }  ,fill opacity=0.67 ] (174.24,96.9) .. controls (174.24,91.63) and (188.72,87.36) .. (206.57,87.36) .. controls (224.42,87.36) and (238.89,91.63) .. (238.89,96.9) .. controls (238.89,102.16) and (224.42,106.43) .. (206.57,106.43) .. controls (188.72,106.43) and (174.24,102.16) .. (174.24,96.9) -- cycle ;
            	\draw    (151.81,35.41) -- (206.57,96.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (138.63,77.78) .. controls (145.19,83.75) and (161.9,89.72) .. (165.65,74.18) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.17 ] (82.61,154.82) -- (90.53,160.8) -- (69.99,245.16) -- (62.42,240.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.17 ] (146.53,192.8) -- (156.53,192.8) -- (151.24,291.08) -- (140.14,288.56) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.17 ] (341.2,174.13) -- (348.53,172.13) -- (350.08,273.11) -- (342.51,268.07) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.17 ] (85.87,202.13) -- (143.67,238.09) -- (143.34,240.68) -- (78.06,204.78) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.2 ]   (279.93,199.23) -- (341.2,228.13) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.35 ]   (158.53,227.47) -- (315.25,215.78) ;
            	\draw (141.48,15) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (245.7,123.81) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (148.55,161) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (227.64,97.33) node [anchor=north west][inner sep=0.75pt]    {$\alpha $};
            	\draw (192.16,63.94) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {Kính lọc};
            	\draw (101.75,62.13) node [anchor=north west][inner sep=0.75pt]    {$h$};
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Trong quang học, chúng ta đã biết đến định luật quang học về độ chiếu sáng. Nó được phát biểu như sau: Khi một nguồn sáng chiếu lên một mặt phẳng, độ chiếu sáng từ nguồn sáng đến một điểm cho bởi công thức $T = I \cdot \frac{\cos \alpha}{AB^2}$, trong đó $I$ là độ phát sáng của nguồn; $\alpha$ là góc hợp bởi tia sáng và phương thẳng đứng (minh họa như hình vẽ). Một đồng xu được đặt cách ngọn nến một khoảng $BC = %s$ cm. Để tạo hiệu ứng, người ta đặt một tấm kính lọc phía trên đồng xu với hệ số truyền sáng của kính là $k = \sin^2 \alpha$. Hỏi ngọn lửa của cây nến nên đặt ở độ cao bằng bao nhiêu cm để độ sáng thực tế chiếu lên đồng xu là lớn nhất, biết độ sáng thực tế $T' = k \cdot T$?}{%s}''' % (d_val, hinhve))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có: $\\cos \\alpha = \\frac{AC}{AB}$ nên suy ra $T = I \\cdot \\frac{\\cos \\alpha}{AB^2} = I \\cdot \\frac{AC}{AB^3}$, mà $\\sin \\alpha = \\frac{BC}{AB} = \\frac{%s}{AB} \\Rightarrow \\sin^2 \\alpha = \\frac{%s}{AB^2}$. \\\\
            Xét tam giác $ABC$ vuông tại $C$ ta có $AB = \\sqrt{h^2 + %s^2} = \\sqrt{h^2 + %s}$, mặt khác độ sáng thực tế: \\\\
            $T' = k \\cdot T = \\sin^2 \\alpha \\cdot I \\cdot \\frac{AC}{AB^3} = \\frac{%s}{AB^2} \\cdot I \\cdot \\frac{h}{AB^3} = \\frac{%s \\cdot I \\cdot h}{AB^5} = \\frac{%s \\cdot I \\cdot h}{\\left(\\sqrt{h^2 + %s}\\right)^5} = \\frac{%s \\cdot I \\cdot h}{(h^2 + %s)^{\\frac{5}{2}}}$. \\\\
            Để độ sáng thực tế $T'$ chiếu lên đồng xu là lớn nhất thì hàm số $f(h) = \\frac{h}{(h^2 + %s)^{\\frac{5}{2}}}$ phải đạt giá trị lớn nhất (với $h > 0$). \\\\
            Ta tiến hành tính đạo hàm của hàm số $f(h)$: \\\\
            $f'(h) = \\frac{1 \\cdot (h^2 + %s)^{\\frac{5}{2}} - h \\cdot \\frac{5}{2}(h^2 + %s)^{\\frac{3}{2}} \\cdot 2h}{(h^2 + %s)^5} = \\frac{(h^2 + %s)^{\\frac{3}{2}} \\cdot \\left[ (h^2 + %s) - 5h^2 \\right]}{(h^2 + %s)^5} = \\frac{%s - 4h^2}{(h^2 + %s)^{\\frac{7}{2}}}$. \\\\
            Xét $f'(h) = 0 \\Leftrightarrow %s - 4h^2 = 0 \\Leftrightarrow 4h^2 = %s \\Leftrightarrow h^2 = %s \\Rightarrow h = %s$ (do $h > 0$). \\\\
            Qua điểm $h = %s$, đạo hàm $f'(h)$ đổi dấu từ dương sang âm nên hàm số đạt cực đại tại $h = %s$. \\\\
            Vậy ngọn lửa của cây nến cần đặt ở độ cao $h = %s$ cm thì độ sáng thực tế chiếu lên đồng xu là lớn nhất.''' 
                % (d_val, d_sq, d_val, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, d_sq, kq**2, kq, kq, kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

