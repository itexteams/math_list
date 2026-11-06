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


def bt_dang35_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM HỆ SỐ ---
                # Cấu trúc: (a*n^3 - b*n) / (c*n^2 + d*n - e)
                # Để đảm bảo kết quả là +vc như bài mẫu, a và c cùng dấu dương.
                n=symbols('n')
                a = random.randint(2, 5)      # Hệ số của n^3 trên tử
                b = random.randint(2, 9)      # Hệ số của n trên tử (để trừ)

                c = random.randint(2, 5)      # Hệ số của n^2 dưới mẫu
                d = random.randint(2, 5)      # Hệ số của n dưới mẫu
                e = random.randint(2, 9)      # Hằng số dưới mẫu (để trừ)

                # Tạo biểu thức symbolic để hiển thị đề bài
                Tu = a * n**3 - b * n
                Mau = c * n**2 + d * n - e

                # --- BƯỚC 2: TÍNH TOÁN KẾT QUẢ VÀ TẠO NHIỄU ---
                # Kết quả đúng
                kq_dung = "+\\infty" 

                # Các phương án nhiễu
                # Nhiễu 1: -vc (sai dấu)
                nhieu_1 = "-\\infty"
                # Nhiễu 2: 0 (sai bậc)
                nhieu_2 = "0"
                # Nhiễu 3: Tỉ số hệ số bậc cao nhất (bẫy học sinh tưởng cùng bậc) -> a/c
                nhieu_3 = latex(sp.Rational(a, c))

                # Danh sách đáp án cho hiển thị
                du = ['$%s$' % kq_dung]

                # Tập hợp các đáp án sai
                s = ['$%s$' % nhieu_1,
                     '$%s$' % nhieu_2,
                     '$%s$' % nhieu_3]

                da = du[0] # Đáp án đúng

                # Random vị trí đáp án sai
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- BƯỚC 3: XÂY DỰNG NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ("Giới hạn $L = \\lim_{n \\to +\\infty} \\frac{%s}{%s}$ bằng" 
                                 % (latex(Tu), latex(Mau)))

                # --- BƯỚC 4: XÂY DỰNG LỜI GIẢI CHI TIẾT ---
                # Logic lời giải: Chia cả tử và mẫu cho n^3 (lũy thừa cao nhất của tử)
                # Tử sau khi chia: a - b/n^2
                tu_sau_chia = "%s - \\frac{%s}{n^2}" % (a, b) if a != 1 else "1 - \\frac{%s}{n^2}" % b

                # Mẫu sau khi chia: c/n + d/n^2 - e/n^3
                mau_sau_chia = "\\frac{%s}{n} + \\frac{%s}{n^2} - \\frac{%s}{n^3}" % (c, d, e)

                loigiai = (r'''Ta có: $L = \lim_{n \to +\infty} \frac{%s}{%s} 
                           = \lim_{n \to +\infty} \frac{%s}{%s} = +\infty.$''' 
                           % (latex(Tu), latex(Mau), tu_sau_chia, mau_sau_chia))

                # --- BƯỚC 5: TRỘN ĐÁP ÁN VÀ XUẤT RA ---
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xuất câu trắc nghiệm theo format
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choice \n'
                    '{' + str(list_1[0]).replace('\\True ', '') + '}\n'
                    '{' + str(list_1[1]).replace('\\True ', '') + '}\n'
                    '{' + str(list_1[2]).replace('\\True ', '') + '}\n'
                    '{' + str(list_1[3]).replace('\\True ', '') + '}\n'
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')

                # Xử lý lại dòng \True để khớp với tool thi trắc nghiệm (nếu tool cần \True nằm trong ngoặc)
                # Đoạn code trên đang replace mất \True khi in vào choice, ta cần logic in đúng vị trí.
                # Sửa lại phần in choice:

                content_fixed = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choice \n')

                for item in list_1:
                    content_fixed += '{' + item + '}\n'

                content_fixed += ('\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content

