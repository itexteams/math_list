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


def bt_dang13_p4_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo ngẫu nhiên 2 nghiệm x1, x2 để đảm bảo biểu thức trong căn luôn có 2 nghiệm phân biệt
                x1 = random.randint(-5, -1)
                x2 = random.randint(1, 5)

                # Biểu thức trong căn là - (x - x1)(x - x2) = -x^2 + (x1 + x2)x - x1*x2
                b = x1 + x2
                c = -x1 * x2

                # Tính tọa độ cực trị (x_mid là trung điểm của 2 nghiệm)
                x_mid = Rational(b, 2)
                y_max = sqrt(-x_mid**2 + b*x_mid + c)

                # Hàm số và đạo hàm
                f_expr = -x**2 + b*x + c
                f_prime_num = -2*x + b

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = \\sqrt{%s}$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (latex(f_expr)))

                # Các đáp án trắc nghiệm
                da = '(%s; %s)' % (latex(x1), latex(x_mid))
                das1 = '(%s; %s)' % (latex(x_mid), latex(x2))
                das2 = '(-\\infty; %s)' % (latex(x_mid))
                das3 = '(%s; %s)' % (latex(x1), latex(x2))

                da_d = ('\\True $%s$' % str(da))
                da_s1 = '$%s$' % str(das1)
                da_s2 = '$%s$' % str(das2)
                da_s3 = '$%s$' % str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tập xác định: $D = [%s; %s]$. \\\\
                    Ta có $y' = \\frac{%s}{2\\sqrt{%s}}$. \\\\
                    \\hspace*{1.1cm} $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$. \\\\
                    \\hspace*{1.1cm} $y'$ không xác định tại $x = %s$, $x = %s$. \\\\
                    Bảng biến thiên:
                    \\begin{center}
                    \\begin{tikzpicture}[>=stealth, line width=1pt]
                    \\def\\w{1.5}
                    \\def\\c{2.6}
                    \\draw (0,0) rectangle (\\w+4*\\c, -3.5);
                    \\draw (0,-1) -- (\\w+4*\\c, -1);
                    \\draw (0,-2) -- (\\w+4*\\c, -2);
                    \\draw (\\w,0) -- (\\w,-3.5);
                    \\node at (\\w/2, -0.5) {$x$};
                    \\node at (\\w/2, -1.5) {$y'$};
                    \\node at (\\w/2, -2.75) {$y$};
                    \\node at (\\w+0.15*\\c, -0.5) {$-\\infty$};
                    \\node at (\\w+1*\\c, -0.5) {$%s$};
                    \\node at (\\w+2*\\c, -0.5) {$%s$};
                    \\node at (\\w+3*\\c, -0.5) {$%s$};
                    \\node at (\\w+3.8*\\c, -0.5) {$+\\infty$};
                    \\begin{scope}
                        \\clip (\\w, -1) rectangle (\\w+1*\\c, -3.5);
                        \\foreach \\i in {10, 12, ..., 70}
                            \\draw[thin] (\\i/10, -1) -- (\\i/10 - 2.5, -3.5);
                    \\end{scope}
                    \\begin{scope}
                        \\clip (\\w+3*\\c+0.08, -1) rectangle (\\w+4*\\c, -3.5);
                        \\foreach \\i in {85, 87, ..., 150}
                            \\draw[thin] (\\i/10, -1) -- (\\i/10 - 2.5, -3.5);
                    \\end{scope}
                    \\draw (\\w+1*\\c, -1) -- (\\w+1*\\c, -3.5);
                    \\draw (\\w+3*\\c, -1) -- (\\w+3*\\c, -3.5);
                    \\draw (\\w+1*\\c+0.08, -1) -- (\\w+1*\\c+0.08, -2);
                    \\draw (\\w+3*\\c+0.08, -1) -- (\\w+3*\\c+0.08, -2);
                    \\node at (\\w+1.5*\\c, -1.5) {$+$};
                    \\node at (\\w+2*\\c, -1.5) {$0$};
                    \\node at (\\w+2.5*\\c, -1.5) {$-$};
                    \\node (A) at (\\w+1*\\c+0.4, -3.1) {$0$};
                    \\node (B) at (\\w+2*\\c, -2.4) {$%s$};
                    \\node (C) at (\\w+3*\\c-0.4, -3.1) {$0$};
                    \\draw[->] (A) -- (B);
                    \\draw[->] (B) -- (C);
                    \\end{tikzpicture}
                    \\end{center}
                    Từ bảng biến thiên ta thấy \\\\
                    \\hspace*{1.1cm} Hàm số đồng biến trên khoảng $\\left(%s; %s\\right)$. \\\\
                    \\hspace*{1.1cm} Hàm số nghịch biến trên khoảng $\\left(%s; %s\\right)$. \\\\
                    \\hspace*{1.1cm} Hàm số đạt cực đại tại $x = %s$; $y_{\\text{CĐ}} = %s$.''' %
                    (
                     latex(x1), latex(x2),                       
                     latex(f_prime_num), latex(f_expr),          
                     latex(f_prime_num), latex(x_mid),           
                     latex(x1), latex(x2),                       
                     latex(x1), latex(x_mid), latex(x2),         
                     latex(y_max),                               
                     latex(x1), latex(x_mid),                    
                     latex(x_mid), latex(x2),                    
                     latex(x_mid), latex(y_max)                               
                    ))

            elif dang=='2':
                # Khởi tạo ngẫu nhiên 2 nghiệm x1, x2 (để tạo tam thức bậc 2 có a > 0)
                x1 = random.randint(-5, 0)
                x2 = random.randint(1, 5)

                # Biểu thức trong căn là (x - x1)(x - x2) = x^2 - (x1 + x2)x + x1*x2
                b = -(x1 + x2)
                c = x1 * x2

                # Nghiệm của tử số đạo hàm
                x_mid = Rational(-b, 2)

                # Hàm số và đạo hàm
                f_expr = x**2 + b*x + c
                f_prime_num = 2*x + b

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = \\sqrt{%s}$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (latex(f_expr)))

                # Các đáp án trắc nghiệm 
                da = '(%s; +\\infty)' % (latex(x2))
                das1 = '(-\\infty; %s)' % (latex(x1))
                das2 = '(%s; %s)' % (latex(x1), latex(x2))
                das3 = '(%s; +\\infty)' % (latex(x_mid))

                da_d = ('\\True $%s$' % str(da))
                da_s1 = '$%s$' % str(das1)
                da_s2 = '$%s$' % str(das2)
                da_s3 = '$%s$' % str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tập xác định: $D = (-\\infty; %s] \\cup [%s; +\\infty)$. \\\\
                    Ta có $y' = \\frac{%s}{2\\sqrt{%s}}$. \\\\
                    \\hspace*{1.1cm} $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$ (không thuộc $D$). \\\\
                    \\hspace*{1.1cm} $y'$ không xác định tại $x = %s$, $x = %s$. \\\\
                    Bảng biến thiên:
                    \\begin{center}
                    \\begin{tikzpicture}[>=stealth, line width=1pt]
                    \\def\\w{1.5}
                    \\def\\c{2.6}
                    \\draw (0,0) rectangle (\\w+3*\\c, -3.5);
                    \\draw (0,-1) -- (\\w+3*\\c, -1);
                    \\draw (0,-2) -- (\\w+3*\\c, -2);
                    \\draw (\\w,0) -- (\\w,-3.5);
                    \\node at (\\w/2, -0.5) {$x$};
                    \\node at (\\w/2, -1.5) {$y'$};
                    \\node at (\\w/2, -2.75) {$y$};
                    \\node at (\\w+0.15*\\c, -0.5) {$-\\infty$};
                    \\node at (\\w+1*\\c, -0.5) {$%s$};
                    \\node at (\\w+2*\\c, -0.5) {$%s$};
                    \\node at (\\w+2.8*\\c, -0.5) {$+\\infty$};
                    \\begin{scope}
                        \\clip (\\w+1*\\c+0.08, -1) rectangle (\\w+2*\\c-0.08, -3.5);
                        \\foreach \\i in {35, 37, ..., 100}
                            \\draw[thin] (\\i/10, -1) -- (\\i/10 - 2.5, -3.5);
                    \\end{scope}
                    \\draw (\\w+1*\\c, -1) -- (\\w+1*\\c, -3.5);
                    \\draw (\\w+2*\\c, -1) -- (\\w+2*\\c, -3.5);
                    \\draw (\\w+1*\\c+0.08, -1) -- (\\w+1*\\c+0.08, -2);
                    \\draw (\\w+2*\\c-0.08, -1) -- (\\w+2*\\c-0.08, -2);
                    \\node at (\\w+0.5*\\c, -1.5) {$-$};
                    \\node at (\\w+2.5*\\c, -1.5) {$+$};
                    \\node (A) at (\\w+0.2*\\c, -2.4) {$+\\infty$};
                    \\node (B) at (\\w+1*\\c-0.3, -3.1) {$0$};
                    \\node (C) at (\\w+2*\\c+0.3, -3.1) {$0$};
                    \\node (D) at (\\w+2.8*\\c, -2.4) {$+\\infty$};
                    \\draw[->] (A) -- (B);
                    \\draw[->] (C) -- (D);
                    \\end{tikzpicture}
                    \\end{center}
                    Từ bảng biến thiên ta thấy \\\\
                    \\hspace*{1.1cm} Hàm số đồng biến trên khoảng $\\left(%s; +\\infty\\right)$. \\\\
                    \\hspace*{1.1cm} Hàm số nghịch biến trên khoảng $\\left(-\\infty; %s\\right)$. \\\\
                    \\hspace*{1.1cm} Hàm số không có cực trị.''' %
                    (
                     latex(x1), latex(x2),                       
                     latex(f_prime_num), latex(f_expr),          
                     latex(f_prime_num), latex(x_mid),           
                     latex(x1), latex(x2),                       
                     latex(x1), latex(x2),                       
                     latex(x2),                                  
                     latex(x1)                                   
                    ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

