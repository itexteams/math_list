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


def bt_dang50_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Danh sách các bộ kích thước hình hộp chữ nhật (x, y, z) tạo ra các số liệu đẹp
                params = [
                    (20, 40, 30),  # Đề bài gốc trong ảnh: AB=20sqrt(5), AC=50, AD=10sqrt(13)
                    (10, 20, 30),
                    (15, 20, 60),
                    (10, 24, 30),
                    (18, 24, 40),
                    (30, 40, 50),
                    (12, 16, 15)
                ]

                x_val, y_val, z_val = random.choice(params)

                # Bình phương các cạnh của tứ diện gần đều
                a_sq = x_val**2 + y_val**2
                b_sq = y_val**2 + z_val**2
                c_sq = z_val**2 + x_val**2

                # Rút gọn căn thức bằng SymPy
                a_sym = sp.sqrt(a_sq)
                b_sym = sp.sqrt(b_sq)
                c_sym = sp.sqrt(c_sq)

                # Thể tích hình hộp và thể tích tứ diện
                V_box = x_val * y_val * z_val
                V_ans = sp.Rational(1, 3) * V_box

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(V_ans))]
                da = random.choice(du)

                s = [
                    '$%s$' % (latex(V_box)),
                    '$%s$' % (latex(sp.Rational(1, 6) * V_box)),
                    '$%s$' % (latex(V_ans + 1000)),
                    '$%s$' % (latex(V_ans - 500 if V_ans > 500 else V_ans + 500)),
                    '$%s$' % (latex(V_ans * 2)),
                    '$%s$' % (latex(V_ans + 2000))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Hình vẽ TikZ
                tikz_str = ('''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw  [line width=1]  (85.5,102) -- (221.1,102) -- (221.1,190.4) -- (85.5,190.4) -- cycle ;
                		\\draw [line width=1]    (85.5,102) -- (140.1,56.4) ;
                		\\draw [line width=1]    (221.1,102) -- (275.7,56.4) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (85.5,190.4) -- (140.1,144.8) ;
                		\\draw [line width=1]    (221.1,190.4) -- (275.7,144.8) ;
                		\\draw [line width=1]    (140.1,56.4) -- (275.7,56.4) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (140.1,144.8) -- (275.7,144.8) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (140.1,56.4) -- (140.1,144.8) ;
                		\\draw [line width=1]    (275.7,56.4) -- (275.7,144.8) ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (275.7,56.4) -- (85.5,102) ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (275.7,56.4) -- (221.1,190.4) ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (221.1,190.4) -- (85.5,102) ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (85.5,102) -- (140.1,144.8) ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (140.1,144.8) -- (272.6,58.4) ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (140.1,144.8) -- (224.6,190.9) ;
                		\\draw (65.5,88) node [anchor=north west][inner sep=0.75pt]    {$A$};
                		\\draw (275.5,38) node [anchor=north west][inner sep=0.75pt]    {$B$};
                		\\draw (215.5,193) node [anchor=north west][inner sep=0.75pt]    {$C$};
                		\\draw (114,134.5) node [anchor=north west][inner sep=0.75pt]    {$D$};
                	\\end{tikzpicture}
                \\end{center}''')

                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện $ABCD$ có $AB = CD = %s$, $AC = BD = %s$, $AD = BC = %s$. Thể tích của khối tứ diện đã cho bằng bao nhiêu?'''
                                 % (latex(a_sym), latex(b_sym), latex(c_sym)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''%s
            Nhận xét tứ diện $ABCD$ có các cặp cạnh đối bằng nhau:\\\\
            $AB = CD = %s$\\\\
            $AC = BD = %s$\\\\
            $AD = BC = %s$\\\\
            Dựng hình hộp chữ nhật ngoại tiếp tứ diện $ABCD$ có các kích thước lần lượt là $x, y, z > 0$.\\\\
            Khi đó, các cạnh của tứ diện $ABCD$ là đường chéo các mặt của hình hộp chữ nhật.\\\\
            Ta có hệ phương trình:\\\\
            $\\begin{cases} x^2 + y^2 = %s \\\\ y^2 + z^2 = %s \\\\ z^2 + x^2 = %s \\end{cases}$\\\\
            Cộng từng vế của ba phương trình, ta được:\\\\
            $2(x^2 + y^2 + z^2) = %s \\Leftrightarrow x^2 + y^2 + z^2 = %s.$\\\\
            Từ đó suy ra:\\\\
            $\\begin{cases} z^2 = %s - %s = %s \\Rightarrow z = %s \\\\ x^2 = %s - %s = %s \\Rightarrow x = %s \\\\ y^2 = %s - %s = %s \\Rightarrow y = %s \\end{cases}$\\\\
            Thể tích hình hộp chữ nhật là:\\\\
            $V_{\\text{hộp}} = x \\cdot y \\cdot z = %s \\cdot %s \\cdot %s = %s.$\\\\
            Thể tích khối tứ diện $ABCD$ là:\\\\
            $V = \\frac{1}{3} V_{\\text{hộp}} = \\frac{1}{3} \\cdot %s = %s.$'''
                           % (
                               tikz_str,
                               latex(a_sym), latex(b_sym), latex(c_sym),
                               a_sq, b_sq, c_sq,
                               2 * (x_val**2 + y_val**2 + z_val**2), x_val**2 + y_val**2 + z_val**2,
                               x_val**2 + y_val**2 + z_val**2, a_sq, z_val**2, z_val,
                               x_val**2 + y_val**2 + z_val**2, b_sq, x_val**2, x_val,
                               x_val**2 + y_val**2 + z_val**2, c_sq, y_val**2, y_val,
                               x_val, y_val, z_val, V_box,
                               V_box, latex(V_ans)
                           ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(V_ans))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

