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


def bt_dang62_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                k = random.choice([1, 2, 3, 4, 5])
                v0 = 7 * k

                if v0 == 7:
                    V_str = '\\frac{7\\sqrt{6}}{2}'
                else:
                    V_str = '\\frac{%s\\sqrt{6}}{2}' % (v0)

                u_val = 0.7645466776120889
                x_val = (2 * (k**2) * u_val)**(1/6)
                kq = round(x_val, 2)
                kq_str = f"{kq:.2f}".replace('.', ',')

                #Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da = random.choice(du)

                # Generate false options by adding/subtracting small amounts
                s = [
                     '$%s$'%(f"{round(x_val + 0.15, 2):.2f}".replace('.', ',')),
                     '$%s$'%(f"{round(x_val + 0.24, 2):.2f}".replace('.', ',')),
                     '$%s$'%(f"{round(x_val + 0.32, 2):.2f}".replace('.', ',')),
                     '$%s$'%(f"{round(x_val - 0.12, 2):.2f}".replace('.', ',')),
                     '$%s$'%(f"{round(x_val - 0.21, 2):.2f}".replace('.', ',')),
                     '$%s$'%(f"{round(x_val - 0.28, 2):.2f}".replace('.', ',')),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một hình chóp cụt lục giác đều có thể tích là $%s$ cạnh đáy lớn có độ dài gấp hai lần cạnh đáy nhỏ. Khi trải phẳng hình chóp cụt lục giác đều trên một mặt phẳng thì đáy lớn nội tiếp trên 1 đường tròn (như hình vẽ). Độ dài cạnh đáy nhỏ của hình chóp cụt lục giác đều bằng bao nhiêu biết đường tròn ngoại tiếp đáy lớn có bán kính đạt giá trị nhỏ nhất? (kết quả làm tròn đến hàng phần trăm).
            \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.21 ][line width=1]  (353.3,118.2) -- (474.3,153.2) -- (485.8,197.7) -- (425.3,221.2) -- (350,219.5) -- (312.8,178.2) -- cycle ;
            		\\draw  [line width=1]  (59.3,131.5) .. controls (59.3,79.2) and (101.7,36.8) .. (154,36.8) .. controls (206.3,36.8) and (248.7,79.2) .. (248.7,131.5) .. controls (248.7,183.8) and (206.3,226.2) .. (154,226.2) .. controls (101.7,226.2) and (59.3,183.8) .. (59.3,131.5) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (210.3,131.5) -- (182.15,180.26) -- (125.85,180.26) -- (97.7,131.5) -- (125.85,82.74) -- (182.15,82.74) -- cycle ;
            		\\draw [line width=1]    (125.85,82.74) -- (119.8,43.2) ;
            		\\draw [line width=1]    (96.3,57.2) -- (125.85,82.74) ;
            		\\draw [line width=1]    (59.8,143.7) -- (97.7,131.5) ;
            		\\draw [line width=1]    (97.7,131.5) -- (60.3,119.2) ;
            		\\draw [line width=1]    (115.3,217.7) -- (125.85,180.26) ;
            		\\draw [line width=1]    (96.8,206.2) -- (125.85,180.26) ;
            		\\draw [line width=1]    (192.3,217.7) -- (182.15,180.26) ;
            		\\draw [line width=1]    (182.15,180.26) -- (213.3,206.2) ;
            		\\draw [line width=1]    (182.15,82.74) -- (191.8,45.2) ;
            		\\draw [line width=1]    (209.3,54.2) -- (182.15,82.74) ;
            		\\draw [line width=1]    (248.3,121.7) -- (210.3,131.5) ;
            		\\draw [line width=1]    (248.3,141.7) -- (210.3,131.5) ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (451.3,174.2) -- (425.3,220.7) -- (350,219.5) -- (312.8,177.7) -- (289.8,102.7) -- (329.8,43.2) -- (431.8,43.2) -- (477.3,101.2) -- cycle ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]    (289.8,102.7) -- (340.3,141.2) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]    (340.3,141.2) -- (350,219.5) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]    (340.3,141.2) -- (432.8,141.2) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]    (432.8,141.2) -- (425.3,220.7) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]    (432.8,141.2) -- (477.3,101.2) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (329.8,43.2) -- (351.3,132.2) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (431.8,43.2) -- (415.3,132.2) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (351.3,132.2) -- (415.3,132.2) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (351.3,132.2) -- (312.8,177.7) ;
            		\\draw [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (415.3,132.2) -- (449.3,176.7) ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (96.3,57.2) -- (125.85,82.74) -- (97.7,131.5) -- (60.3,119.2) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (191.8,45.2) -- (182.15,82.74) -- (125.85,82.74) -- (119.8,43.2) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (209.3,54.2) -- (248.3,121.7) -- (210.3,131.5) -- (182.15,82.74) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (210.3,131.5) -- (248.3,141.7) -- (213.3,206.2) -- (182.15,180.26) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (125.85,180.26) -- (182.15,180.26) -- (192.3,217.7) -- (115.3,217.7) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (97.7,131.5) -- (125.85,180.26) -- (96.8,206.2) -- (59.8,143.7) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.15 ][line width=1]  (289.8,103.2) -- (340.3,141.7) -- (350,220) -- (312.8,178.2) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.15 ][line width=1]  (340.3,141.7) -- (432.8,141.7) -- (425.3,221.2) -- (350,220) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.15 ][line width=1]  (432.8,141.2) -- (477.3,101.2) -- (449.3,176.7) -- (425.3,220.7) -- cycle ;
            	\\end{tikzpicture}
            \\end{center}'''
                                 %(V_str))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi độ dài cạnh đáy nhỏ của hình chóp cụt lục giác đều là $x$ ($x > 0$). \\\\
                Vì cạnh đáy lớn gấp hai lần cạnh đáy nhỏ nên độ dài cạnh đáy lớn là $2x$. \\\\
                Diện tích đáy nhỏ là $S_1 = 6 \\cdot \\frac{x^2\\sqrt{3}}{4} = \\frac{3\\sqrt{3}}{2}x^2$. \\\\
                Diện tích đáy lớn là $S_2 = 6 \\cdot \\frac{(2x)^2\\sqrt{3}}{4} = 6\\sqrt{3}x^2$. \\\\
                Thể tích hình chóp cụt là \\\\$V = \\frac{1}{3} h (S_1 + S_2 + \\sqrt{S_1 S_2}) = \\frac{1}{3} h \\left( \\frac{3\\sqrt{3}}{2}x^2 + 6\\sqrt{3}x^2 + 3\\sqrt{3}x^2 \\right) = \\frac{7\\sqrt{3}}{2} h x^2$. \\\\
                Theo giả thiết $V = %s$, suy ra $h = \\frac{%s\\sqrt{2}}{7x^2}$. \\\\
                Trung đoạn của hình chóp cụt (đường cao của mặt bên) là \\\\$l = \\sqrt{h^2 + \\left( x\\sqrt{3} - \\frac{x\\sqrt{3}}{2} \\right)^2} = \\sqrt{\\frac{%s}{x^4} + \\frac{3}{4}x^2}$. \\\\
                Khi trải phẳng, đáy lớn là các cạnh bên ngoài của các hình thang cân, nằm trên đường tròn tâm là tâm của đáy nhỏ. Khoảng cách từ tâm đến cạnh đáy ngoài là $d = \\frac{x\\sqrt{3}}{2} + l$. \\\\
                Bán kính đường tròn ngoại tiếp phần trải phẳng là $R_c = \\sqrt{d^2 + x^2}$. \\\\
                Ta có hàm số $f(x) = R_c^2 = \\left( \\frac{x\\sqrt{3}}{2} + \\sqrt{\\frac{%s}{x^4} + \\frac{3}{4}x^2} \\right)^2 + x^2$ với $x > 0$. \\\\
                Sử dụng máy tính cầm tay để tìm giá trị nhỏ nhất của hàm số $f(x)$ hoặc giải phương trình đạo hàm $f'(x)=0$, ta tìm được $x \\approx %s$ thì bán kính $R_c$ đạt giá trị nhỏ nhất. \\\\
                Vậy độ dài cạnh đáy nhỏ xấp xỉ $%s$.'''
                         %(V_str, v0, 2*k**2, 2*k**2, kq_str, kq_str))

            dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

