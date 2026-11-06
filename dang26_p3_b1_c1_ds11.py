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


def bt_dang26_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tử số và mẫu số để tạo các phân số cos khác nhau cho hai góc nhọn
                # Đảm bảo cos nhỏ hơn 1
                m_a = random.randint(3, 6)
                m_b = random.randint(4, 7)
                while m_a == m_b:
                    m_b = random.randint(4, 7)

                cos_a = Rational(1, m_a)
                cos_b = Rational(1, m_b)

                # Tính giá trị biểu thức P = cos^2(a) + cos^2(b) - 1
                P_val = cos_a**2 + cos_b**2 - 1

                # Lấy tử số và mẫu số tối giản của P
                tu_so = abs(P_val.p)
                mau_so = P_val.q

                # Kết quả bài toán yêu cầu tính tổng tử số và mẫu số
                kq_nguyen = tu_so + mau_so
                da = '$%s$' % (latex(kq_nguyen))

                # Tạo các đáp án trắc nghiệm nhiễu
                s = [
                    '$%s$' % (latex(kq_nguyen + random.randint(2, 5))),
                    '$%s$' % (latex(kq_nguyen - random.randint(2, 4))),
                    '$%s$' % (latex(mau_so - tu_so)),
                    '$%s$' % (latex(tu_so + mau_so + 2)),
                    '$%s$' % (latex(tu_so * 2 + mau_so)),
                    '$%s$' % (latex(kq_nguyen + 10))
                ]

                # Lọc bỏ các phần tử trùng với đáp án đúng và lọc trùng
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi định dạng bằng %s
                noidungcauhoi = ('''Cho hai góc nhọn $a$ và $b$. Biết $\\cos a = %s$ và $\\cos b = %s$. Tính giá trị của $P = (\\cos a \\cdot \\cos b)^2 - (\\sin a \\cdot \\sin b)^2$, ta được $P = \\frac{a_0}{b_0}$ (với $\\frac{a_0}{b_0}$ là phân số tối giản và $b_0 > 0$). Giá trị của $a_0 + b_0$ bằng bao nhiêu?'''
                                 % (latex(cos_a), latex(cos_b)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có các công thức lượng giác cơ bản liên hệ giữa $\\sin$ và $\\cos$: \\\\
                           $\\sin^2 a = 1 - \\cos^2 a$ \\\\
                           $\\sin^2 b = 1 - \\cos^2 b$. \\\\
                           Biến đổi biểu thức $P$ ban đầu như sau: \\\\
                           $P = \\cos^2 a \\cdot \\cos^2 b - \\sin^2 a \\cdot \\sin^2 b$ \\\\
                           $\\Leftrightarrow P = \\cos^2 a \\cdot \\cos^2 b - (1 - \\cos^2 a)(1 - \\cos^2 b)$ \\\\
                           $\\Leftrightarrow P = \\cos^2 a \\cdot \\cos^2 b - (1 - \\cos^2 a - \\cos^2 b + \\cos^2 a \\cdot \\cos^2 b)$ \\\\
                           $\\Leftrightarrow P = \\cos^2 a + \\cos^2 b - 1$. \\\\
                           Thay giả thiết $\\cos a = %s$ và $\\cos b = %s$ vào biểu thức đã rút gọn, ta thu được: \\\\
                           $P = \\left(%s\\right)^2 + \\left(%s\\right)^2 - 1 = %s + %s - 1 = %s$. \\\\
                           Do phân số thu được là tối giản, nên ta xác định được: \\\\
                           $a_0 = %s$ và $b_0 = %s$. \\\\
                           Vậy giá trị của tổng $a_0 + b_0 = %s + %s = %s$.'''
                           % (latex(cos_a), latex(cos_b), latex(cos_a), latex(cos_b), 
                              latex(cos_a**2), latex(cos_b**2), latex(P_val), 
                              latex(tu_so), latex(mau_so), latex(tu_so), latex(mau_so), latex(kq_nguyen)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_nguyen))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

