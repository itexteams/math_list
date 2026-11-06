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


def bt_dang16_p3_b5_c2_hh11(self):
            # Khai báo biến
            # a: cạnh đáy, h: chiều cao khối lăng trụ
            a = random.randint(2, 5)
            h = random.randint(1, 3)

            # Tính khoảng cách d
            # h_base = a * sqrt(3) / 2
            # 1/d^2 = 1/h_base^2 + 1/h^2 = 4/(3*a^2) + 1/h^2 = (4*h^2 + 3*a^2) / (3*a^2*h^2)
            # d = sqrt(3*a^2*h^2 / (4*h^2 + 3*a^2))
            h_base_sq = 3 * a**2 / 4
            d_sq = 1 / (1 / h_base_sq + 1 / h**2)
            d = sqrt(d_sq)

            # Định dạng hiển thị kết quả và các phương án
            # Chuyển đổi sang chuỗi LaTeX, thay dấu chấm bằng dấu phẩy nếu cần
            def format_num(val):
                return str(val).replace('.', ',')

            kq = h
            # Tạo các phương án nhiễu
            wrong1 = h + 1
            wrong2 = h + 2
            wrong3 = h - 1 if h > 1 else h + 3

            # Danh sách đáp án
            du = ['$%s$' % (format_num(kq))]
            s = ['$%s$' % (format_num(wrong1)),
                 '$%s$' % (format_num(wrong2)),
                 '$%s$' % (format_num(wrong3)),
                 '$%s$' % (format_num(round(float(d), 2))),
                 '$%s$' % (format_num(round(float(a), 2)))]

            random.shuffle(s)
            da = du[0]
            das1, das2, das3 = s[0], s[1], s[2]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một khối đá có dạng hình lăng trụ tam giác đều $ABC.A'B'C'$ với cạnh đáy bằng $%s$ dm, khoảng cách từ điểm $A'$ đến mặt phẳng $(AB'C')$ bằng $%s$ dm. Khoảng cách giữa hai mặt phẳng đáy của khối đá hình lăng trụ đã cho theo đơn vị deximet bằng bao nhiêu?'''
                             % (latex(a), latex(format_num(round(float(d), 2)))))


            # Lời giải chi tiết
            loigiai = ('''\\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw [line width=1]    (66.68,39.52) -- (224.67,39.52) ;
            		\\draw [line width=1]    (66.68,39.52) -- (138.38,102.97) ;
            		\\draw [line width=1]    (138.38,102.97) -- (224.67,39.52) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (66.68,191.8) -- (224.67,191.8) ;
            		\\draw [line width=1]    (66.68,191.8) -- (138.38,255.25) ;
            		\\draw [line width=1]    (138.38,255.25) -- (224.67,191.8) ;
            		\\draw [line width=1]    (66.68,39.52) -- (66.68,191.8) ;
            		\\draw [line width=1]    (138.38,102.97) -- (138.38,255.25) ;
            		\\draw [line width=1]    (224.67,39.52) -- (224.67,191.8) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (224.67,39.52) -- (66.68,191.8) ;
            		\\draw [line width=1]    (224.67,39.52) -- (138.38,255.25) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (224.67,39.52) -- (102.53,223.53) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (224.67,191.8) -- (102.53,223.53) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (224.67,191.8) -- (158.05,141.67) ;
            		\\draw (229.51,19.76) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (118.2,98.44) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (46.63,17.86) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\\draw (228.28,179.02) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            		\\draw (129.66,256.43) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            		\\draw (39.69,180.93) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            		\\draw (83.7,225.34) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\\draw (138,122.55) node [anchor=north west][inner sep=0.75pt]    {$K$};		
            	\\end{tikzpicture}
            \\end{center}
            Trong $(A'B'C')$, kẻ $A'H \\perp B'C'$ tại $H$ và trong $(AA'H)$, kẻ $A'K \\perp AH$ tại $K$. \\\\
                        Ta có: $\\begin{cases} B'C' \\perp A'H \\\\ B'C' \\perp AA' (\\text{do } AA' \\perp (A'B'C')) \\end{cases} \\Rightarrow B'C' \\perp (AA'H) \\Rightarrow A'K \\perp B'C'$. \\\\
                        Từ đó suy ra $A'K \\perp (AB'C')$ hay $d(A', (AB'C')) = A'K = %s$ dm. \\\\
                        Xét tam giác $A'B'C'$ đều có đường cao $A'H = \\frac{%s\\sqrt{3}}{2}$ dm. \\\\
                        Tam giác $AA'H$ vuông tại $A'$ có đường cao $A'K$ nên \\\\
                        $\\frac{1}{A'K^2} = \\frac{1}{A'H^2} + \\frac{1}{A'A^2} \\Rightarrow A'A = %s$ dm. \\\\
                        Hai mặt phẳng đáy song song với nhau và có khoảng cách là $d((ABC), (A'B'C')) = AA' = %s$ dm.''' % (latex(format_num(round(float(d), 2))), latex(a), latex(h), latex(h)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(h))
            # Các đáp án
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi) +dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

