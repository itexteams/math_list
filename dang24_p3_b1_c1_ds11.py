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


def bt_dang24_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số nhân k để làm phong phú bài toán
                k = random.randint(1, 5)

                # Biến số để thay vào f(val), giá trị val không làm đổi kết quả
                val = random.randint(1, 2026)

                # Biến đổi biểu thức gốc: k * [3*(1 - 2s^2c^2) - 2*(1 - 3s^2c^2)] = k * [3 - 2] = k
                hso_1 = 3 * k
                hso_2 = 2 * k

                kq_nguyen = k
                da = '$%s$' % (latex(kq_nguyen))

                # Tạo các phương án trắc nghiệm nhiễu
                s = [
                    '$%s$' % (latex(kq_nguyen + 1)),
                    '$%s$' % (latex(kq_nguyen - 1)),
                    '$%s$' % (latex(0)),
                    '$%s$' % (latex(2 * kq_nguyen)),
                    '$%s$' % (latex(-kq_nguyen)),
                    '$%s$' % (latex(k + 2))
                ]

                # Lọc bỏ phần tử trùng đáp án đúng và lọc trùng
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi định dạng chuỗi bằng %s
                noidungcauhoi = ('''Cho biểu thức $f(x) = %s(\\sin^4 x + \\cos^4 x) - %s(\\sin^6 x + \\cos^6 x)$. Giá trị của $f(%s)$ bằng bao nhiêu?'''
                                 % (latex(hso_1), latex(hso_2), latex(val)))

                # Các phương án trả lời
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn thứ tự các phương án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước bằng tiếng Việt, xuống dòng bằng \\\\
                loigiai = ('''Sử dụng các hằng đẳng thức lượng giác cơ bản: \\\\
                           $\\sin^4 x + \\cos^4 x = (\\sin^2 x + \\cos^2 x)^2 - 2\\sin^2 x \\cos^2 x = 1 - 2\\sin^2 x \\cos^2 x$. \\\\
                           $\\sin^6 x + \\cos^6 x = (\\sin^2 x + \\cos^2 x)^3 - 3\\sin^2 x \\cos^2 x (\\sin^2 x + \\cos^2 x) = 1 - 3\\sin^2 x \\cos^2 x$. \\\\
                           Thay vào biểu thức $f(x)$, ta được: \\\\
                           $f(x) = %s(1 - 2\\sin^2 x \\cos^2 x) - %s(1 - 3\\sin^2 x \\cos^2 x)$ \\\\
                           $\\Leftrightarrow f(x) = %s - %s\\sin^2 x \\cos^2 x - %s + %s\\sin^2 x \\cos^2 x$ \\\\
                           $\\Leftrightarrow f(x) = %s - %s = %s$. \\\\
                           Do biểu thức $f(x)$ luôn nhận giá trị không đổi với mọi $x$, hằng số $f(x) = %s$. \\\\
                           Do đó, ta có $f(%s) = %s$.'''
                           % (latex(hso_1), latex(hso_2), latex(hso_1), latex(2*hso_1), latex(hso_2), latex(3*hso_2), latex(hso_1), latex(hso_2), latex(kq_nguyen), latex(kq_nguyen), latex(val), latex(kq_nguyen)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_nguyen))
            # Xuất câu trắc nghiệm đúng định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

