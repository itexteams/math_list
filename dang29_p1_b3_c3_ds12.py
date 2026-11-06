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


def bt_dang29_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bán kính R. Chọn R là số nguyên để biểu thức đẹp, hoặc số chia hết cho 2
                # Trong đề gốc R=3. Ta random R từ 2 đến 10.
                R = random.randint(2, 10)

                # Tính toán theo công thức thể tích phần chung: V = 2 * tích phân từ R/2 đến R của pi*(R^2 - x^2)dx
                # Kết quả lý thuyết: V = 5/12 * pi * R^3
                R_half = Rational(R, 2)
                R2 = R**2

                # Tính toán giá trị đúng
                tu_so = 5 * (R**3)
                mau_so = 12
                kq_fraction = Rational(tu_so, mau_so)
                da_dung = '$%s \\pi$' % (latex(kq_fraction))

                # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    # Các phương án nhiễu phổ biến: quên nhân 2 (giống hình mẫu), nhầm hệ số, nhầm lũy thừa
                    sai1 = '$%s \\pi$' % (latex(Rational(5 * R**3, 24))) # Quên nhân 2 (giống lời giải trong ảnh)
                    sai2 = '$%s \\pi$' % (latex(Rational(R**3, 3)))
                    sai3 = '$%s \\pi$' % (latex(Rational(7 * R**3, 12)))
                    sai4 = '$%s \\pi$' % (latex(Rational(R**3, 4)))

                    temp_list = [sai1, sai2, sai3, sai4]
                    selected = random.choice(temp_list)
                    if selected != da_dung:
                        s.add(selected)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hai mặt cầu $(S_1), (S_2)$ có cùng bán kính $R = %s$ thỏa mãn tính chất tâm của $(S_1)$ thuộc $(S_2)$ và ngược lại. Thể tích $V$ phần chung của hai khối cầu tạo bởi $(S_1), (S_2)$ bằng'''
                                 %(latex(R)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Lưu ý: dx thay bằng \text{d}x theo yêu cầu
                loigiai=(r'''\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw    (106.67,168.67) -- (364.67,168.67) ;
            					\draw [shift={(366.67,168.67)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw    (206.67,248.67) -- (206.67,90.67) ;
            					\draw [shift={(206.67,88.67)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw   (146.77,168.77) .. controls (146.77,135.68) and (173.58,108.87) .. (206.67,108.87) .. controls (239.75,108.87) and (266.57,135.68) .. (266.57,168.77) .. controls (266.57,201.85) and (239.75,228.67) .. (206.67,228.67) .. controls (173.58,228.67) and (146.77,201.85) .. (146.77,168.77) -- cycle ;
            					\draw   (206.67,168.67) .. controls (206.67,135.58) and (233.48,108.77) .. (266.57,108.77) .. controls (299.65,108.77) and (326.47,135.58) .. (326.47,168.67) .. controls (326.47,201.75) and (299.65,228.57) .. (266.57,228.57) .. controls (233.48,228.57) and (206.67,201.75) .. (206.67,168.67) -- cycle ;
            					\draw    (238.4,118.13) -- (237.73,170.13) ;
            					\draw (186.67,168.67) node [anchor=north west][inner sep=0.75pt]    {$O$};
            					\draw (266.57,168.67) node [anchor=north west][inner sep=0.75pt]    {$O'$};
            					\draw (225.33,92.33) node [anchor=north west][inner sep=0.75pt]    {$A$};
            					\draw (227.33,223.33) node [anchor=north west][inner sep=0.75pt]    {$B$};
            					\draw (226.67,168.67) node [anchor=north west][inner sep=0.75pt]    {$H$};
            					\draw (343.33,170.67) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (187.33,85) node [anchor=north west][inner sep=0.75pt]    {$y$};
            				\end{tikzpicture}
            			\end{center}
                        Phần chung của hai khối cầu tạo bởi $(S_1), (S_2)$ là một khối tròn xoay, tương đương phần hình phẳng giới hạn bởi đường tròn tâm $O$ bán kính $R=%s$ quay quanh trục nối hai tâm. \\
                          Đặt hệ trục tọa độ sao cho tâm $O(0;0)$ và $O'(%s;0)$. \\
                          Phương trình đường tròn $(O)$ là $x^2 + y^2 = %s \Rightarrow y^2 = %s - x^2$.\\
                          Giao điểm của hai đường tròn có hoành độ là $H$ với $x_H = \frac{R}{2} = %s$.\\
                          Thể tích phần chung bằng hai lần thể tích chỏm cầu từ $%s$ đến $%s$:\\
                          $V = 2\pi \int_{%s}^{%s} (%s - x^2) \text{d}x = 2\pi \left( %s x - \frac{x^3}{3} \right) \bigg|_{%s}^{%s} = %s \pi$.'''
                          %(latex(R), latex(R), latex(R2), latex(R2), 
                            latex(R_half), latex(R_half), latex(R),
                            latex(R_half), latex(R), latex(R2), 
                            latex(R2), latex(R_half), latex(R), latex(kq_fraction)
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

