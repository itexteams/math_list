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


def bt_dang31_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random bài toán
                # Cạnh hình vuông ban đầu (chọn số để diện tích là số nguyên)
                a = random.randint(2, 6) 
                # Số lần chia (thường chọn 2 hoặc 3 để phù hợp với trình độ trắc nghiệm và lời giải)
                n = random.randint(2, 3) 

                # Diện tích ban đầu
                S_bd = a**2

                # Công thức tổng quát diện tích phần tô màu sau n lần: S = S_bd * (1 - (8/9)^n)
                dien_tich_to = Rational(S_bd) * (1 - Rational(8, 9)**n)

                # Đáp án đúng
                da = '$%s$' % latex(dien_tich_to)

                # B4: Tạo các phương án sai (không được trùng đáp án đúng)
                s = [
                    '$%s$' % latex(Rational(S_bd * (8**(n-1)), 9**n)),          # Chỉ tính diện tích của lần cuối
                    '$%s$' % latex(Rational(S_bd * (8**n), 9**n)),              # Diện tích phần CHƯA tô màu
                    '$%s$' % latex(Rational(S_bd * (1 - Rational(8, 9)**(n-1)))), # Quên bước chia cuối cùng
                    '$%s$' % latex(Rational(dien_tich_to.p + 1, dien_tich_to.q)), # Sai lệch tử số
                    '$%s$' % latex(Rational(S_bd, 9**n)),                        # Sai công thức lũy thừa
                    '$%s$' % latex(Rational(S_bd * n, 9)),                       # Sai logic tăng trưởng
                ]

                # Lọc bỏ nếu vô tình trùng với đáp án đúng
                s = [item for item in s if item != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một hình vuông có cạnh bằng $%s$. Chia hình vuông đó thành $9$ hình vuông bằng nhau và tô màu hình vuông ở chính giữa. 
                    Với mỗi hình vuông nhỏ chưa được tô màu, lại chia thành $9$ hình vuông bằng nhau và tô màu hình vuông ở chính giữa. 
                    Cứ như thế, quá trình trên được lặp lại. Diện tích phần được tô màu sau $%s$ lần chia bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).}
                                 {\begin{tikzpicture}[scale=1.3]
            	\fill[orange] (1,1) rectangle (2,2);
            	\foreach \i in {0,1,2}{
            		\foreach \j in {0,1,2}{
            			\ifnum\i=1\ifnum\j=1\else
            			\fill[orange] (\i+1/3,\j+1/3) rectangle ++(1/3,1/3);
            			\fi\else
            			\fill[orange] (\i+1/3,\j+1/3) rectangle ++(1/3,1/3);
            			\fi
            	}}
            	\foreach \i in {0,1,2}{
            		\foreach \j in {0,1,2}{
            			\ifnum\i=1\ifnum\j=1\else
            			\foreach \a in {0,1,2}{
            				\foreach \b in {0,1,2}{
            					\ifnum\a=1\ifnum\b=1\else
            					\fill[orange] (\i+\a/3+1/9,\j+\b/3+1/9) rectangle ++(1/9,1/9);
            					\fi\else
            					\fill[orange] (\i+\a/3+1/9,\j+\b/3+1/9) rectangle ++(1/9,1/9);
            					\fi
            			}}
            			\fi\else
            			\foreach \a in {0,1,2}{
            				\foreach \b in {0,1,2}{
            					\ifnum\a=1\ifnum\b=1\else
            					\fill[orange] (\i+\a/3+1/9,\j+\b/3+1/9) rectangle ++(1/9,1/9);
            					\fi\else
            					\fill[orange] (\i+\a/3+1/9,\j+\b/3+1/9) rectangle ++(1/9,1/9);
            					\fi
            			}}
            			\fi
            	}}
            	\draw[thick] (0,0) rectangle (3,3);
            	\foreach \x in {1,2}{
            		\draw[thick] (\x,0)--(\x,3);
            		\draw[thick] (0,\x)--(3,\x);
            	}
            	\foreach \x in {1/3,2/3,4/3,5/3,7/3,8/3}{
            		\draw (\x,0)--(\x,3);
            		\draw (0,\x)--(3,\x);
            	}
            	\fill[orange] (1,1) rectangle (2,2);
            \end{tikzpicture}}'''
                    % (latex(a), latex(n))
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Xây dựng dựa trên n lần)
                # Ở đây giả định n=2 hoặc n=3 để viết lời giải chi tiết
                s1 = Rational(S_bd, 9)
                s2 = Rational(8 * S_bd, 81)
                s3 = Rational(64 * S_bd, 729)

                if n == 2:
                    h1=dien_tich_to
                    number = Decimal(float(h1))  # Số cần làm tròn
                    kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    kqz=str(kq1).replace('.', ',')
                    loigiai = (
                        'Diện tích hình vuông ban đầu là $S = %s^2 = %s$.\\\\ \n'
                        'Lần chia thứ nhất: Tô màu $1$ hình vuông trung tâm có diện tích $S_1 = \\frac{1}{9} S = %s$.\\\\ \n'
                        'Số hình vuông chưa được tô màu là $8$. \\\\ \n'
                        'Lần chia thứ hai: Với mỗi hình vuông chưa tô, ta lại tô $1$ hình vuông nhỏ ở giữa. \\\\ \n'
                        'Tổng diện tích tô thêm ở lần hai là $S_2 = 8 \\cdot \\left( \\frac{1}{9} \\cdot \\frac{S}{9} \\right) = %s$.\\\\ \n'
                        'Tổng diện tích phần được tô màu sau $2$ lần chia là: \\\\ \n'
                        '$S_{\\text{tổng}} = S_1 + S_2 = %s + %s = %s \\approx %s$.'
                        % (latex(a), latex(S_bd), latex(s1), latex(s2), latex(s1), latex(s2), latex(dien_tich_to), str(kqz))
                    )
                    #Đáp án
                    dapan=' \\shortans[0]{$%s$} '%(kqz)
                else: # Trường hợp n=3
                    h1=dien_tich_to
                    number = Decimal(float(h1))  # Số cần làm tròn
                    kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    kqz=str(kq1).replace('.', ',')
                    loigiai = (
                        'Diện tích hình vuông ban đầu là $S = %s^2 = %s$.\\\\ \n'
                        'Lần chia thứ nhất: Tô màu diện tích $S_1 = \\frac{1}{9}S = %s$. Còn lại $8$ hình vuông nhỏ.\\\\ \n'
                        'Lần chia thứ hai: Tô thêm diện tích $S_2 = 8 \\cdot \\frac{S}{81} = %s$. Còn lại $8^2 = 64$ hình vuông nhỏ.\\\\ \n'
                        'Lần chia thứ ba: Tô thêm diện tích $S_3 = 64 \\cdot \\frac{S}{729} = %s$.\\\\ \n'
                        'Tổng diện tích phần được tô màu sau $3$ lần chia là: \\\\ \n'
                        '$S_{\\text{tổng}} = S_1 + S_2 + S_3 = %s + %s + %s = %s \\approx %s$.'
                        % (latex(a), latex(S_bd), latex(s1), latex(s2), latex(s3), latex(s1), latex(s2), latex(s3), latex(dien_tich_to), str(kqz))
                    )
                    #Đáp án
                    dapan=' \\shortans[0]{$%s$} '%(kqz)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

