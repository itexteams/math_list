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


def bt_dang37_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # n là tổng số học sinh, k là số cặp anh em sinh đôi
                n = randint(35, 45) 
                k = randint(3, 6)

                # Tính toán các giá trị theo logic bài toán
                # Số phần tử không gian mẫu
                n_omega = n * (n - 1) * (n - 2) // 6

                # Biến cố đối A_gạch: Có 1 cặp anh em sinh đôi được chọn
                # Chọn 1 cặp trong k cặp, chọn 1 học sinh còn lại trong (n-2) học sinh
                n_A_gach = k * (n - 2)

                # Số phần tử của biến cố A: Không có cặp anh em nào
                n_A = n_omega - n_A_gach

                # Xác suất
                prob = Rational(n_A, n_omega)
                prob_gach = Rational(n_A_gach, n_omega)

                # Bước 4: Điều chỉnh các phương án sai không được trùng đáp án đúng
                da = '$%s$' % (latex(prob))

                # Tạo danh sách các phương án sai
                s = [
                    '$%s$' % (latex(prob_gach)), # Xác suất của biến cố đối
                    '$%s$' % (latex(Rational(n_A - 2, n_omega))),
                    '$%s$' % (latex(Rational(n_A + 5, n_omega + 10))),
                    '$%s$' % (latex(Rational(n_A - 10, n_omega))),
                    '$%s$' % (latex(Rational(1, n_omega // n_A_gach if n_omega % n_A_gach == 0 else 100)))
                ]

                # Loại bỏ các giá trị trùng với đáp án đúng (nếu có)
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi (B2 - Viết lại y hệt cấu trúc)
                # Không dùng tiền tố r (raw string), thay dấu ngoặc theo yêu cầu
                noidungcauhoi = ('Một lớp học có %s học sinh trong đó có %s cặp anh em sinh đôi. Trong buổi họp đầu năm thầy giáo chủ nhiệm muốn chọn ra 3 học sinh để làm cán sự lớp gồm lớp trưởng, lớp phó và bí thư. Xác suất để chọn ra 3 học sinh làm cán sự lớp mà không có cặp anh em sinh đôi nào bằng'
                                 % (latex(n), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Chi tiết, không viết tắt, thay . bằng ,)
                loigiai = ('Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{3} = %s$. \\\\ '
                           'Gọi $A$ là biến cố “chọn ra 3 học sinh làm cán sự lớp mà không có cặp anh em sinh đôi nào”. \\\\ '
                           'Biến cố $\\bar{A}$ là 3 học sinh được chọn luôn có 1 cặp anh em sinh đôi. \\\\ '
                           '- Chọn 1 cặp anh em sinh đôi trong %s cặp có $C_{%s}^{1}$ cách. \\\\ '
                           '- Chọn thêm 1 học sinh trong %s học sinh còn lại, có $C_{%s}^{1}$ cách. \\\\ '
                           'Suy ra số phần tử của biến cố $\\bar{A}$ là $n\\left(\\bar{A}\\right) = C_{%s}^{1}C_{%s}^{1} = %s$. \\\\ '
                           'Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s - %s = %s$. \\\\ '
                           'Vậy xác suất cần tính $P\\left(A\\right) = \\frac{%s}{%s} = %s$.'
                           % (latex(n), latex(n_omega),
                              latex(k), latex(k),
                              latex(n - 2), latex(n - 2),
                              latex(k), latex(n - 2), latex(n_A_gach),
                              latex(n_omega), latex(n_A_gach), latex(n_A),
                              latex(n_A), latex(n_omega), latex(prob)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

